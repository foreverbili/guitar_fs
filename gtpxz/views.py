from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def detail(request,gtp_id):
    return HttpResponse('兴趣使然的指弹交♂流社区' + gtp_id + request.GET.get('a',gtp_id))


def index(request):
    kmap={}
    users = models.Users.objects.all()
    kmap['users']=users
    user_name=request.GET.get('name')
    if user_name:
        current_user=models.Users.objects.get(name=user_name)
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
            return HttpResponse("Register Success")
    content = {}
    content['form']=form
    return render(request,'gtpxz/register.html',content)


    # users = models.Users.objects.all()
    # html = [x.name+'\n' for x in users]
    # return HttpResponse(html)
