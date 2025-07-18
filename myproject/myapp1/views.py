from django.shortcuts import render
from django.http import HttpResponse
from .models import Individual, Department
from .forms import IndividualForm

# Create your views here.
def hello_func(request):
    return HttpResponse("hello, steve.!")

def start(request):
    dic_1 = {
        'list' : ['randy', 'edge', 'rock', 'kurt angle']
    }
    return render(request, "start.html", dic_1)

def last(request):
    dic_2 = {
        'author' : 'johnny',
        'birthplace' : 'sydney',
        'age' : 34
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