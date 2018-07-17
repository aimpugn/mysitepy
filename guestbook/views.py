from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
from guestbook.models import Guestbook

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.


def list(request):
    # id 역순으로 정렬하여 모든 리스트 반환
    guestbooks = Guestbook.objects.all().order_by('-id')
    length = len(guestbooks)

    # map 생성하여 반환
    data = {'guestbooks': guestbooks, 'length': length}
    return render(request, 'guestbook/list.html', data)


def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.content = request.POST['content']
    guestbook.time = datetime.now()

    guestbook.save()

    return HttpResponseRedirect('/guestbook')


def deleteform(request):
    no = request.GET['no']
    logger.info('no: ', no)
    data = {'no': no}
    return render(request, 'guestbook/deleteform.html', data)


def delete(request):
    no = request.POST['no']
    if no is not None:
        Guestbook.objects.filter(id=no).filter(password=request.POST['password']).delete()

    return HttpResponseRedirect("/guestbook")
