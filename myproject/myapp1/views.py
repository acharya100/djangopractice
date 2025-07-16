from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'link.html')

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