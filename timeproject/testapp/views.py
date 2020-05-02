from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import datetime

def wish(request):
    date=datetime.datetime.now()
    msg='hello this is ratna bharathi time very'
    h=int(date.strftime('%H'))
    if h<12:
        msg +='Morning'
    elif h<16:
        msg +='AfterNoon'
    elif h<21:
        msg +='Evening'
    else:
        msg='hello guest good night'
    s="<h1>{} and time is {}</h1>".format(msg,date)
    return HttpResponse(s)
