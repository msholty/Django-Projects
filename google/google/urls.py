from django.conf.urls.defaults import *
from django.conf.urls import patterns, url
from searchengine.views import *

urlpatterns = patterns('',
	url(r'^/?$', search),
)