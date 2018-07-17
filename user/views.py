from django.forms import model_to_dict
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from user.models import User


def joinform(request):
    return render(request, 'user/joinform.html')


def loginform(request):
    return render(request, 'user/loginform.html')


def login(request):
    result = User\
        .objects\
        .filter(email=request.POST['email'])\
        .filter(password=request.POST['password'])

    # 로그인 실패
    if len(result) < 1:
        return HttpResponseRedirect('/user/loginform?result=false')

    # 로그인 성공
    auth_user = result[0]
    # 세션 사용시 setting.py의 MIDDLEWARE에 'django.contrib.sessions.middleware.SessionMiddleware' 있는지 확인
    # DB에 저장되기 때문에 브라우저를 종료해도 로그인 상태가 살아있다.
    request.session['auth_user'] = model_to_dict(auth_user)
    return HttpResponseRedirect('/')


def logout(request):
    #  세션 삭제
    del request.session['auth_user']
    return HttpResponseRedirect('/')


def join(request):
    user = User()
    user.email = request.POST['email']
    user.password = request.POST['password']
    user.name = request.POST['name']
    user.gender = request.POST['gender']

    user.save()

    return HttpResponseRedirect('/user/joinsuccess')


def joinsuccess(request):
    return render(request, 'user/joinsuccess.html')
