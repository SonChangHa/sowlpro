from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 글 작성자가 누구인지
    #title = models.CharField(max_length=200)  # 글의 제목, 최대 크기 200이하의 캐릭터필드
    #text = models.TextField()  # 글의 내용, 최대 크기 제한 없는 텍스트필드
    #created_date = models.DateTimeField(
      #      default=timezone.now)  # 생성날짜
    #published_date = models.DateTimeField(
     #       blank=True, null=True)  # 게시날짜

    def publish(self):
        self.published_date = timezone.now()
        self.save()  # 날짜에 현재 누르면 나오는거(?맞나)

    def __str__(self):
        return self.title  # 제목 리턴
