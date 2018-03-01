from django.conf.urls import url
from gtpxz import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<gtp_id>\d+)/', views.detail, name='detail')
]
