from django.urls import path
from . import views

urlpatterns = [
    path('table/free/', views.free_table, name='free_table'),
    path('table/free/new/', views.freeTable_new, name='free_new'),
    path('table/notice/new/', views.noticeTable_new, name='notice_new'),
    path('table/free/<int:pk>/', views.post_detail, name='post_detail'),
    path('table/photo/', views.photo_table, name='photo_table'),
    path('table/rule/', views.rule_table, name='rule_table'),

]


