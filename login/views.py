from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.contrib.auth import login, authenticate
from .forms import LoginForm
# login과 authenticate 기능을 사용하기위해 선언
# login은 login처리를 해주며, authenticate는 아이디와 비밀번호가 모두 일치하는 User 객체를 추출


def login_menu(request):  # 로그인 기능
    if request.method == "GET":
        return render(request, 'login/login_menu.html', {'f': SigninForm()})

    elif request.method == "POST":
        form = SigninForm(request.POST)
        id = request.POST['username']
        pw = request.POST['password']
        u = authenticate(username=id, password=pw)
        # authenticate를 통해 DB의 username과 password를 클라이언트가 요청한 값과 비교한다.
        # 만약 같으면 해당 객체를 반환하고 아니라면 none을 반환한다.

        if u:  # u에 특정 값이 있다면
            login(request, user=u)  # u 객체로 로그인해라
            return HttpResponseRedirect(reverse('vote:index'))
        else:
            return render(request, 'login/login_menu.html', {'f': form, 'error': '아이디나 비밀번호가 일치하지 않습니다.'})