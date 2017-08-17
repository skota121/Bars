from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<rapper>[-\w]+)/$', views.detail, name='detail'),
    url(r'^(?P<rapper>[-\w]+)/(?P<music>[-\w]+)/$', views.results, name='results' )

]