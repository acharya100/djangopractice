from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Individual, Department
from .forms import IndividualForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as log, logout
from django.contrib.auth.decorators import login_required
from .decorators import admin_only
from rest_framework.views import APIView 
# Create your views here.

def hello_func(request):
    return HttpResponse("hello, steve.!")

@admin_only
def start(request):
    dic_1 = {
        'list' : ['randy', 'edge', 'rock', 'kurt angle', 'big show']
    }
    return render(request, "start.html", dic_1)

def last(request):
    dic_2 = {
        'author' : 'johnny',
        'birthplace' : 'sydney',
        'age' : 34,
        'info':["john","cena",48]
    }
    return render(request, "last.html",dic_2)


def link(request):
    i=Individual.objects.all()[:3]
    return render(request,'link.html',{'Individual':i})

def navbar(request):
    return render(request, 'navbar.html')

def home(request):
    return render(request, 'home.html')

def company(request):
    return render(request, 'company.html')

def marketplace(request):
    return render(request, 'marketplace.html')

def contact(request):
    return render(request, 'contact.html')

def features(request):
    return render(request, 'features.html')

def team(request):
    return render(request, 'team.html')

def department(request):
    if request.method =="POST":
        name=request.POST.get("name")
        dep=Department.objects.create(name=name)
        dep.save()
    return render(request, 'department.html')


def Individual_view(request):
    if request.method=="POST":
        form=IndividualForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form=IndividualForm()

    return render(request,"Individual.html",{'form':form})

@login_required
def Individual_list(request):
    Individual1=Individual.objects.all()
    return render(request,'Individual_list.html',{'Individual':Individual1})


def edit(request,i_id):
    instance=Individual.objects.get(id=i_id)
    if request.method == "POST":
        form=IndividualForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return redirect("Individual_list")
    form=IndividualForm(instance=instance)


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username,password=password)
        user.save()
        return redirect('login')
    return render(request,"signup.html")

def login(request):
    if request.method =="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            log(request,user)
            if user.is_staff:
                return redirect('Individual_list')
            else:
                return redirect('link')
    return render(request,"login.html")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
  
    
def delete(request,id):
    data=Individual.objects.get(id=id)
    data.delete()
    return redirect('Individuallist')

def error404(request, exception):
    return render(request, 'error404.html')

def error500(request):
    return render(request, 'error500.html')

