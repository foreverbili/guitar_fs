from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login


# Create your views here.

def detail(request,gtp_id):
    return HttpResponse('兴趣使然的指弹交♂流社区' + gtp_id + request.GET.get('a',gtp_id))


def index(request):
    kmap={}
    users = models.User.objects.all()
    kmap['users']=users
    user_name=request.GET.get('name')
    if user_name:
        current_user=models.User.objects.get(name=user_name)
    elif len(users)>0:
        current_user=users[0]
    kmap['current_user']=current_user
    return render(request,'gtpxz/gtpxz.html',kmap)

def index_register(request):
    if request.method == "GET":
        form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print (form.is_valid())
        if form.is_valid():
            form.save()
            return redirect(to="index")
    content = {}
    content['form']=form
    return render(request,'gtpxz/gtpxz.html',content)

def index_login(request):
    if request.method == "GET":
        form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid(),form.error_messages)
        if form.is_valid():
            login(request,form.get_user())
            return HttpResponse("Login Success")
    content = {}
    content['form']=form
    return render(request,'gtpxz/gtpxz.html',content)


    # users = models.Users.objects.all()w
    # html = [x.name+'\n' for x in users]
    # return HttpResponse(html)
