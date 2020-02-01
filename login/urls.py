from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_menu, name='login_menu'),

]