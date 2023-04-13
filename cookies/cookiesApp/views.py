from django.shortcuts import render
from datetime import timedelta,datetime

def home(Request):
    return render(Request,'home.html')


def setcookies(Request):
    request = render(Request,'setcookies.html')
    request.set_cookie('name','Rahul Gupta',max_age=30)
    request.set_cookie('email','rahul.g89@yahoo.com',max_age=30)
    request.set_cookie('phone','9818110450',max_age=30)
    request.set_cookie('salary',25000,max_age=30)
    return request


def getcookies(Request):
    name = Request.COOKIES.get('name',None)
    email = Request.COOKIES.get('email',None)
    phone = Request.COOKIES.get('phone',None)
    salary = Request.COOKIES.get('salary',None)
    return render(Request,'getcookies.html',{'name':name,'email':email,'phone':phone,'salary':salary})


def deletecookies(Request):
    request = render(Request,'deletecookies.html')
    if(Request.COOKIES.get('name',None)):
        request.delete_cookie('name')
    if(Request.COOKIES.get('email',None)):
        request.delete_cookie('name')
    if(Request.COOKIES.get('phone',None)):
        request.delete_cookie('name')
    if(Request.COOKIES.get('salary',None)):
        request.delete_cookie('name')
    return request
