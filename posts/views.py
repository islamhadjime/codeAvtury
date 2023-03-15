from django.shortcuts import render, get_object_or_404 
from django.db.models import Count
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request,'posts/home.html',{'posts':posts})


def detail_post(request,pk):
    post  = get_object_or_404(Post,pk=pk)
    print(post)
    context = {
        'post':post,
    }

    return render(request,'posts/detail.html',context)