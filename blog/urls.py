from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.blg_list, name='blg_list'),
    url(r'^blog/', views.blog, name='blog'),

]