from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from blog import models as blgm
from video import models as vidm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.conf import settings
from .forms import GtpForm

# Create your views here.

def index_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            u = form.save()
            models.Profile.objects.create(user=u)
            return redirect(to="index")
    else:
        form = UserCreationForm()
    content = {}
    content['form'] = form
    return render(request,'gtpxz/gtpxz.html',content)

def index_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect(to="index")
    else:
        form = AuthenticationForm()
    content = {}
    content['form']=form
    return render(request,'gtpxz/gtpxz.html',content)

def index(request):
    blogs = blgm.Blog.objects.all().order_by('-id')[:8]
    vids = vidm.Video.objects.all().order_by('-id')[:8]
    gtps = models.Gtp.objects.all().order_by('-id')[:8]
    keymap = {}
    keymap['blogs'] = blogs
    keymap['vids'] = vids
    keymap['gtps'] = gtps
    return render(request, 'gtpxz/gtpxz.html', keymap)

def index_logout(request):
    logout(request)
    return redirect(to="index")

def upload_gtp(request):
    if request.method == 'POST':
        # gtp = request.FILES['gtp']
        form = GtpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # gtp_path = '%s/%s' % (settings.MEDIA_ROOT, gtp.name)
            # with open(gtp_path , 'wb') as f:
            #     for chunk in gtp.chunks():
            #         f.write(chunk)
        return HttpResponse('success')
    else:
        form = GtpForm()
    return render(request, 'gtpxz/upload_gtp.html', {'form': form})


    # users = models.Users.objects.all()w
    # html = [x.name+'\n' for x in users]
    # return HttpResponse(html)
