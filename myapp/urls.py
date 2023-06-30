
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('confirm', views.index, name='confirm'),
    path('regist', views.index, name='regist'),
]
