from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello there I heard you have a backlog of movies and shows you need to catch up on!</h1>')

def about(request):
  return render(request, 'about.html')

def shows_index(request):
  return render(request, 'shows/index.html', { 'shows': shows })

class Show:
  def __init__(self, title, type, description, runtime, episodes, complete):
    self.title = title
    self.type = type
    self.description = description
    self.runtime = runtime
    self.episodes = episodes
    self.complete = complete

shows = [
  Show('Book of Boba Fett', 'TV Series', 'Package for Bob A Feet', 40, 1, 'no' ),
  Show('The Mandalorian', 'TV Series', 'Baby Yoda is evil', 40, 16, 'yes' ),
  Show('Eternals', 'Movie', 'MCU meets GOT characters', 157, 1, 'no' ),
  Show('No Way Home', 'Movie', 'Live action Into the Spiderverse', 148, 1, 'yes' ),
]