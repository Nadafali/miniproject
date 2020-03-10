from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.forms import RegisterForms
from .models import loginmodel

# Create your views here.

def login(request):
    if request.method == "POST":
        usid = request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = loginmodel.objects.get(username=usid, password=pswd)
            request.session['username'] = check.id
            return redirect('home')
        except:
            pass
    return render(request, 'login.html')


def register(request, id=0):
    if request.method == "GET":
        print("entered if")
        if id == 0:    
            forms = RegisterForms()
        else:
            print("entered else")
            user = loginmodel.objects.get(pk=id)
            forms = RegisterForms(instance=user)
        return render(request, "register.html",{'forms':forms})
    else:
        if id == 0:
            forms = RegisterForms(request.POST)
        else:
            user = loginmodel.objects.get(pk=id)
            forms = RegisterForms(request.POST,instance=user)
        if forms.is_valid():
            forms.save()
        return redirect('profile')



def visitors(request):
    return render(request,'visitors.html')


def home(request):
    return render(request, 'dashboard.html')


def profile(request):
    context = {'profile_list':loginmodel.objects.all()}
    return render(request, "profile.html", context)


def newbook(request):
    return render(request, 'newbook.html')

def bookir(request):
        return render(request,'bookir.html')


def mydetails(request):
    ()

def update_details(request):
    ()
