# blog/urls.py
from django.conf.urls import url
from crawler_web import views

urlpatterns = [
    url(r'^crawler_web/$',  views.index),
    url(r'^register/$',  views.register),
]