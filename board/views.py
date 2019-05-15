from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    post_list = Post.objects.filter(complete_chk=False).order_by('rank')
    post_list_end=Post.objects.filter(complete_chk=True)
    return render(request, 'board/post_list.html',{'post_list':post_list, 'post_list_end':post_list_end})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'board/post_detail.html', {'post':post})

def post_delete(request, id):
    post = Post.objects.get(id = id)
    post.delete()
    return redirect('board:post_list')

def post_add(request):
    total = len(Post.objects.all())
    end = len(Post.objects.filter(rank='end'))
    
    form = PostForm()
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.title = request.POST.get('title')
            post.rank = str(total - end+1)

            # 라디오 버튼 on일 경우, True
            due_chk = False
            if request.POST.get('due_chk')=="on":
                due_chk = True
            post.due_chk = due_chk
            if due_chk:
                post.due_date = request.POST.get('due_date')

            # DB 저장    
            post.save()
            return redirect('board:post_list')
    else :
        form =PostForm()
    return render(request, 'board/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method=="POST":
        form=PostForm(request.POST, instance = post)
        if form.is_valid():
            post=form.save(commit=False)
            post.title = request.POST.get('title')
            
            # 라디오 버튼 on일 경우, True
            due_chk = False
            if request.POST.get('due_chk')=="on":
                due_chk = True
            post.due_chk = due_chk
            if due_chk :
                post.due_date = request.POST.get('due_date')
            
            # 라디오 버튼 on일 경우, True
            complete_chk = False
            if request.POST.get('complete_chk')=="on":
                complete_chk = True
            post.complete_chk=complete_chk
            # DB저장
            post.save()

            # 우선순위 RESET
            rank_chg_aft_complete()
            return redirect('board:post_detail', id=post.pk)
    else :
        form =PostForm(instance=post)
    return render(request, 'board/post_edit.html', {'form':form})


def complete(request, id, url):
    post = Post.objects.get(id= id)
    form = PostForm(instance = post)
    post = form.save(commit=False)
    post.complete_chk = True
    post.rank ='end'
    post.save()

    rank_chg_aft_complete()
    if url == "board:post_detail":
        return redirect(url, id)
        
    return redirect(url)

def rank_chg_aft_complete():
    posts = Post.objects.exclude(complete_chk = True).order_by('rank')
    cnt = 1
    for post in posts:
        form = PostForm(instance = post)
        post = form.save(commit=False)
        post.rank= cnt
        cnt+=1
        post.save()

def post_list_rank_update(request):
    orderlist=request.POST.get('orderlist')
    orderlist=orderlist.split(",")
    
    posts = Post.objects.exclude(complete_chk = True).order_by('rank')
    
    for post in posts:
        form = PostForm(instance = post)
        post = form.save(commit=False)
        post.rank= orderlist.pop(0)
        post.save()

    return HttpResponse("OK")

    


    
