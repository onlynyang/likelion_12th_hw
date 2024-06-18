from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from main.models import Post

from django.contrib.auth.decorators import login_required

def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    followings = user.profile.followings.all()
    followers = user.profile.followers.all()

    context = {
        'user':user,
        'followings': followings,
        'followers': followers,
    }
    return render(request, 'users/mypage.html', context)

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    return render(request, 'main/detail.html', {'post':post})

def follow(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id)
    is_follower = user.profile in followed_user.profile.followers.all()
    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('users:mypage', followed_user.id)

def mypage_redirect(request, id):
    user = get_object_or_404(User, pk=id)
    return redirect('users:mypage', id=id)