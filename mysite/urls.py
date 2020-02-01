from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # 인클루드는 ''이 포함된 url을 ()속에 매핑하라는 뜻, 즉 지금은 아무것도 안적혀있는 ~:8000/을 블로그점유알엘스로 매핑하는것.
]
