from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('destination?<str:nme>&<int:id>', views.destination, name='destination'),
    path('destination', views.destination, name='destination')


]