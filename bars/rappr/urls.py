from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<music>[-\w]+)/$', views.detail, name='detail' )

]