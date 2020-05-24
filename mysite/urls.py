from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('', include('point.urls')),
    path('', include('main.urls')),
    path('', include('write.urls')),
]
