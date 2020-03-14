from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.urls.base import reverse
from .forms import SigninForm
import blog


# login과 authenticate 기능을 사용하기위해 선언
# login은 login처리를 해주며, authenticate는 아이디와 비밀번호가 모두 일치하는 User 객체를 추출


def signin(request):  # 로그인 기능
    if request.method == "GET":
        return render(request, 'login/login_menu.html')

    elif request.method == "POST":
        # id = request.POST['username']
        # pw = request.POST['password']
        # 위 2개의 코드는 유저네임 혹은 비번이 없으면 에러를 일으킴.
        id = request.POST.get('username')
        pw = request.POST.get('password')
        u = authenticate(username=id, password=pw)
        # authenticate를 통해 DB의 username과 password를 클라이언트가 요청한 값과 비교한다.
        # 만약 같으면 해당 객체를 반환하고 아니라면 none을 반환한다.

        if u is not None:  # u에 특정 값이 있다면
            login(request, user=u)  # u 객체로 로그인해라
            return redirect('./')
        else:
            return render(request, 'login/login_menu.html', {'error': '아이디 혹은 비밀번호를 확인해주세요.'})

def signout(request):
    logout(request)
    return redirect('./')