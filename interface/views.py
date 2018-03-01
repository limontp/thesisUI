from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse


from .models import UPost, PPost
from random import randint


labels = ['Sports', 'Religious', 'Traveller', 'Social Activist', 'Extremism', 'Political', 'Writting passion', 'As usual']
cats = 8

def check(ls):
    for l in ls:
        if l != '0':
            return True
    return False

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.method == "POST":
        values = []
        for l in labels:
            values.append(request.POST.get(l, '0'))

        if check(values):
            pid = request.POST.get('pid', '-1')
            st = request.POST.get('status', ' ')
            p = PPost(pid=pid, status=st, label=''.join(values))
            p.save()
            try:
                tmp = UPost.objects.get(pid=pid)
                tmp.r_votes = 0
                tmp.save()
            except:
                pass
    posts = UPost.objects.filter(r_votes__gt=0)
    posts = posts[randint(0, len(posts)-1)]
    return render(request, 'home.html', {'post': posts, 'ls': labels})

def auth(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        uname = request.POST.get('username', '-')
        pword = request.POST.get('password', '-')
        
        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'login.html', {})

'''
1 = Sports
2 = Religious
3 = Traveller
4 = Social Activist
5 = Extremism
6 = Political
7 = Written passion
8 = As usual
'''
