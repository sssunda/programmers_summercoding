from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
import datetime

# Create your views here.
def rank_chg_aft_complete():
    posts = Post.objects.exclude(complete_chk = True).extra({'rank': "CAST(rank as UNSIGNED)"}).order_by('rank')
    cnt = 1
    for post in posts:
        form = PostForm(instance = post)
        post = form.save(commit=False)
        post.rank= cnt
        cnt+=1
        post.save()

def post_list(request):
    # 완료되지 않은 리스트
    post_list = Post.objects.filter(complete_chk=False).extra({'rank': "CAST(rank as UNSIGNED)"}).order_by('rank')
    # 완료된 리스트
    post_list_complete=Post.objects.filter(complete_chk=True).order_by('updated_at')
    # 마감기한 지난 리스트
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    post_list_false=Post.objects.filter(complete_chk=False, due_date__lt=dt).order_by('due_date')

    return render(request, 'board/post_list.html',{'post_list':post_list,'post_list_complete':post_list_complete ,'post_list_false':post_list_false})

def post_detail(request, id):
    post = get_object_or_404(Post,id= id)
    # 마감기한 지난 리스트
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    post_list_false=Post.objects.filter(complete_chk=False, due_date__lt=dt).order_by('due_date')

    return render(request, 'board/post_detail.html', {'post':post, 'post_list_false':post_list_false})

def delete_post(request, id):
    post = get_object_or_404(Post,id= id)
    post.delete()
    rank_chg_aft_complete()
    return redirect('board:post_list')

def add_post(request):
    # 마감기한 지난 리스트
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    post_list_false=Post.objects.filter(complete_chk=False, due_date__lt=dt).order_by('due_date')

    form = PostForm()
    cnt = len(Post.objects.exclude(rank='end'))+1
    
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            if post.complete_chk :
                post.rank='end'
            else :
                post.rank = str(cnt)

            # DB 저장    
            post.save()
            return redirect('board:post_list')
    else :
        form =PostForm()
    return render(request, 'board/post_edit.html', {'form':form ,'post_list_false':post_list_false})

def edit_post(request, pk):
    # 마감기한 지난 리스트
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    post_list_false=Post.objects.filter(complete_chk=False, due_date__lt=dt).order_by('due_date')

    post = get_object_or_404(Post,pk=pk)
    if request.method=="POST":
        form=PostForm(request.POST, instance = post)
        if form.is_valid():
            post=form.save(commit=False)           
                        
            # DB저장
            post.save()

            # 우선순위 RESET
            rank_chg_aft_complete()
            return redirect('board:post_detail', id=post.pk)
    else :
        form =PostForm(instance=post)
    return render(request, 'board/post_edit.html', {'form':form ,'post_list_false':post_list_false})


def complete(request, id, url):
    post = get_object_or_404(Post,id= id)
    form = PostForm(instance = post)
    post = form.save(commit=False)
    post.complete_chk = True
    post.rank ='end'
    
    # DB저장
    post.save()

    # 우선순위 RESET
    rank_chg_aft_complete()
    if url == "board:post_detail":
        return redirect(url, id)
    
    return redirect(url)


def update_post_list_rank(request):
    orderlist=request.POST.get('orderlist')
    orderlist=orderlist.split(",")
    
    posts = Post.objects.exclude(complete_chk = True)
    
    for post in posts:
        form = PostForm(instance = post)
        post = form.save(commit=False)
        post.rank= str(orderlist.index(post.rank)+1)
        post.save()

    return HttpResponse("OK")
