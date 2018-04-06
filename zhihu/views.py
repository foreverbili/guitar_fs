from django.shortcuts import render
from zhihu import models

# Create your views here.
def home(request):
    return render(request,'zhihu/index.html')