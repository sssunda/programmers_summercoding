from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
import datetime

# Create your views here.
def rank_chg_aft_complete():
    posts = Post.objects.exclude(complete_chk = True).order_by('rank')
    cnt = 1
    for post in posts:
        form = PostForm(instance = post)
        post = form.save(commit=False)
        post.rank= cnt
        cnt+=1
        post.save()

def post_list(request):
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    post_list = Post.objects.filter(complete_chk=False).order_by('rank')
    post_list_complete=Post.objects.filter(complete_chk=True).order_by('updated_at')
    post_list_false=Post.objects.filter(complete_chk=False, due_date__lt=dt).order_by('due_date')
    return render(request, 'board/post_list.html',{'post_list':post_list,'post_list_complete':post_list_complete ,'post_list_false':post_list_false})

def post_detail(request, id):
    post = get_object_or_404(Post,id= id)
    return render(request, 'board/post_detail.html', {'post':post})

def delete_post(request, id):
    post = get_object_or_404(Post,id= id)
    post.delete()
    rank_chg_aft_complete()
    return redirect('board:post_list')

def add_post(request):
    total = len(Post.objects.all())
    end = len(Post.objects.filter(rank='end'))
    
    form = PostForm()
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.rank = str(total - end-1)

            # DB 저장    
            post.save()
            return redirect('board:post_list')
    else :
        form =PostForm()
    return render(request, 'board/post_edit.html', {'form':form})

def edit_post(request, pk):
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
    return render(request, 'board/post_edit.html', {'form':form})


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
    
    posts = Post.objects.exclude(complete_chk = True).order_by('rank')
    
    for post in posts:
        form = PostForm(instance = post)
        post = form.save(commit=False)
        post.rank= str(orderlist.index(post.rank)+1)
        post.save()

    return HttpResponse("OK")
