from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime

# Create your views here.
from guestbook.models import Guestbook


def list(request):
    # id 역순으로 정렬하여 모든 리스트 반환
    guestbooks = Guestbook.objects.all().order_by('-id')

    # map 생성하여 반환
    data = {'guestbooks': guestbooks}
    return render(request, 'guestbook/list.html', data)


def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.content = request.POST['content']
    guestbook.time = datetime.now()

    guestbook.save()

    return HttpResponseRedirect('/guestbook')


def delete(request):
    pass