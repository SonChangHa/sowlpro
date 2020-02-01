from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # 쿼리셋의 __lte 는 이하의 값을 보여주는 문구, 즉 지금 시간보다 과거에 작성된 모든 게시물을 불러옴.
    return render(request, 'blog/post_list.html', {'posts': posts})
    # 리퀘스트가 오면 렌더 메소드를 호출하여 포스트 리스트 템플릿을 보여줌
    # {}안쪽은 템플릿을 사용하기 위한 매개변수를 넣음.
