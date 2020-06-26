from django.urls import path
from . import views

urlpatterns = [
    path('table/free', views.free_table, name='free_table'),
    path('write', views.write, name='write'),
]


