from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

def homepage(request):
    return render(request=request,
                  template_name="home.html")



def video(request):
    template = loader.get_template('room_login.html')
    context = {
        'msg': 'Welcome to login page',
    }

    return HttpResponse(template.render(context, request))


def confo(request, roomid, usertype, userref):

    template = loader.get_template('index.html')
    context = {
        'roomId': roomid,
        'user_ref': userref,
        'usertype': usertype,
    }
    return HttpResponse(template.render(context, request))

