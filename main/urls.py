from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('table/free', views.free_table, name='free_table'),

]
