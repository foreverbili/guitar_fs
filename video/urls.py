from django.conf.urls import url
from video import views

urlpatterns = [
    url(r'^$', views.vid_list, name='vid_list'),
    url(r'^video/', views.video, name='video'),

]