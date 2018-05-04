from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
# Create your views here.


def vid_list(request):
    blog = {}
    blogs = models.Video.objects.all()
    blog['name'] = blogs
    blog_name = request.GET.get('name')
    if blog_name:
        current_blog = models.Video.objects.get(name=blog_name)
    elif len(blogs) > 0:
        current_blog = blogs [0]
    else:
        current_blog = 'there is no blog'
    blog['current_blog'] = current_blog
    return render(request, 'gtpxz/blogs.html', blog)


def video(request):
    pass