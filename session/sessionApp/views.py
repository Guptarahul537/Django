from django.shortcuts import render

def home(Request):
    return render(Request,'home.html')


def setsession(Request):
    Request.session['name']='Rahul Gupta'
    Request.session['email']='rahul.g89@yahoo.com'
    Request.session['phone']='9818110450'
    Request.session['salary']=25000
    Request.session.set_expiry(60*60*24*30)
    return render(Request,'setsession.html')


def getsession(Request):
    name = Request.session.get('name',None)
    email = Request.session.get('email',None)
    phone = Request.session.get('phone',None)
    salary = Request.session.get('salary',None)
    return render(Request,'getsession.html',{'name':name,'email':email,'phone':phone,'salary':salary})


def deletesession(Request):
    Request.session.flush()
    return render(Request,'deletesession.html')