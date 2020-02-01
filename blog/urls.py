from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 아무것도 없이 사이트 주소만 입력했을 경우 포스트 리스트를 보여주라는 뜻
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
