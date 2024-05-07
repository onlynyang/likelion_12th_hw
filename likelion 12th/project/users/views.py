from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from main.models import Post

from django.contrib.auth.decorators import login_required

def mypage(request):
    posts = Post.objects.filter(writer=request.user)
    return render(request, 'users/mypage.html', {'posts': posts})

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/detail.html', {'post':post})