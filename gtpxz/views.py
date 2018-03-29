from django.shortcuts import render
from django.shortcuts import HttpResponse
from gtpxz import models
# Create your views here.
def index(request):
    articles = models.Users.objects.all()
    return render(request,'gtpxz/index.html',{'list_list':articles})

def detail(request,gtp_id):
    return HttpResponse('兴趣使然的指弹交♂流社区' + gtp_id + request.GET.get('a',gtp_id))


def home(request):
    return render(request,'guitars.html')