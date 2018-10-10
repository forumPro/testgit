# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from users.forms import RegisterForm
from django.contrib.auth.hashers import make_password,check_password
from users.models import User
import os


# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(user.password)
            user.save()
            return redirect('/user/login/')
        else:
            return render(request,'register.html',{'error':form.errors})
    else:
        return render(request,'register.html')


def user_login(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname').strip()
        password = request.POST.get('password').strip()

        try:
            user = User.objects.get(nickname=nickname)
        except User.DoesNotExist:
            return render(request,'login.html',{'errors':'用户不存在'})

        if check_password(password,user.password):
            request.session['uid'] = user.id
            request.session['nickname'] = user.nickname
            request.session['avatar'] = user.icon.url
            print('icon is {}, icon_type is {}'.format(user.icon.url,type(user.icon.url)))
            return redirect('/user/info/')
        else:
            return render(request, 'login.html', {'errors': '密码错误'})


    else:
        return render(request,'login.html')

def user_logout(request):
    request.session.flush()
    return redirect('/')

def user_info(request):
    uid = request.session.get('uid')
    user = User.objects.get(pk=uid)
    return render(request,'user_info.html',{'user':user})

