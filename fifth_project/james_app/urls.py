from django.urls import path
from django.conf.urls import url
from james_app import views
urlpatterns = [
    url(r'^index',views.index,name='index'),
    url(r'^$',views.base,name='base'),
]
