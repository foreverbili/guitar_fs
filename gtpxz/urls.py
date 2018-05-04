from django.conf.urls import url
from gtpxz import views

urlpatterns = [
    url(r'^$', views.index, name='gtp_list'),
    # url(r'^blog/', views.blog, name='blog'),
    url(r'^gtpup/', views.upload_gtp, name='upload_gtp'),

]

