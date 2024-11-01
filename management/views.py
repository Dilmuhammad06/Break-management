from django.shortcuts import render,redirect
from . models import User
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

limit = 3


@login_required
def index(request):
    user = User.objects.get(id=request.user.id)
    print(timezone.now())
    lunchers = User.objects.filter(lunch_time=True)
    breakers = User.objects.filter(break_time=True)
    calc = timezone.now() - user.time_got
    past = int(calc.total_seconds()) // int(60)
    return render(request, "index.html",{"breakers":breakers,"lunchers":lunchers,"past":past})


@login_required
def break_time(request):
    user = User.objects.get(id=request.user.id)
    total = int(User.objects.filter(break_time=True).count()) + int(User.objects.filter(lunch_time=True).count())

    if user.lunch_time == False and user.break_time == False and total < limit:
        user.break_time = True
        user.time_got = timezone.now()
        user.save()
        return redirect('index')
    else:
        messages.error(request,"Вы не можете взять перерыв или обед")
    return redirect('index')

@login_required
def lunch_time(request):
    user = User.objects.get(id=request.user.id)
    total = int(User.objects.filter(break_time=True).count()) + int(User.objects.filter(lunch_time=True).count())

    if user.break_time == False and user.lunch_time == False and total < limit:
        user.lunch_time = True
        user.time_got = timezone.now()
        user.save()
        return redirect('index')
    else:
        messages.error(request,"Вы не можете взять перерыв или обед")
    return redirect('index')
    


@login_required
def work(request,id):
    if request.user.is_staff:
        user = User.objects.get(id=id)
        user.break_time = False
        user.lunch_time = False
        user.time_got = timezone.now()
        user.save()
        return redirect('index')
    else:
        user = User.objects.get(id=request.user.id)
        user.break_time = False
        user.lunch_time = False
        user.time_got = timezone.now()
        user.save()
        return redirect('index')


class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request,'login.html',{"form":form})

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid username or password.')
        return render(request,'login.html',{"form":form})


class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request,'register.html',{"form":form})

    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
        return render(request,'register.html',{"form":form})

class LogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        return redirect('index')