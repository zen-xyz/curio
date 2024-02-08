from django.shortcuts import render
from blogs.models import Post, Comment

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts' : posts,
    }
    return render(request, 'blogs/index.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        'category':category,
        'posts':posts,
    }
    return render(request, 'blogs/category.html', context)   

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        'post' : post,
        'comments': comments,
    }
    return render(request, 'blogs/detail.html', context)
