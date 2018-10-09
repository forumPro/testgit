# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from math import ceil



# Create your views here.
from post.models import Post


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title,content=content)
        return redirect('/post/read/?post_id=%d' % post.id)
    else:
        return render(request,'create_post.html')

def edit_post(request):
    if request.method == 'POST':
        post_id = int(request.POST.get('post_id'))
        post = Post.objects.get(pk=post_id)

        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('/post/read/?post_id=%d' % post.id)
    else:
        post_id = int(request.GET.get('post_id'))
        post = Post.objects.get(pk=post_id)
        return render(request,'edit_post.html',{'post':post})

def read_post(request):
    post_id = int(request.GET.get('post_id'))
    post = Post.objects.get(pk=post_id)
    return render(request,'read_post.html',{'post':post})



def delete_post(request):
    post_id = int(request.GET.get('post_id'))
    Post.objects.get(pk=post_id).delete()
    return redirect('/')

def post_list(request):
    page = int(request.GET.get('page',1))
    total = Post.objects.count()   #文章总数
    per_page = 10   #每页文章数
    pages = int(ceil(total / per_page)) #总页数

    start= (page-1) * per_page  #当前页开始索引
    end =  start + per_page     #当前页结束索引
    posts = Post.objects.all()[start:end]
    return render(request,'post_list.html',{'posts':posts,
                                            'pages':range(pages+1)})

def search(request):
    keyword = request.POST.get('keyword')
    posts =  Post.objects.filter(content__contains=keyword)
    return render(request,'search.html',{'posts':posts})


