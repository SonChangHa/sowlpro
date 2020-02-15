from django.urls import path
from . import views

urlpatterns = [
    path('test', views.point_list, name='point'),
   # path('test/mine', views.point_list_mine, name='mypoint'),

]