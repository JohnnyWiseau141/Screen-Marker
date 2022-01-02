from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello there I heard you have a backlog of movies and shows you need yo catch up on!</h1>')

def about(request):
  return render(request, 'about.html')