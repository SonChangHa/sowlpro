from django.conf import settings
from django.db import models
from django.utils import timezone
from main.models import table


class Post(models.Model):
    #category = tabl
    #카테고리 추가하기
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='사용자')
    #cascade는 사용자가 삭제되면 해당 글도 지우라는 뜻
    #verbose_name은 관리자 페이지에서 해당 변수가 무엇을 나타내는지 보여주는 것.
    title = models.CharField(max_length=200, verbose_name='제목')
    text = models.TextField(verbose_name='내용')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='작성시간')
    published_date = models.DateTimeField(auto_now=True, verbose_name='수정시간')

    def __str__(self):
        return self.title