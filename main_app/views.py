from django.shortcuts import render

anime = [
  {'title': 'Naruto', 'creator': 'Masashi Kishimoto', 'genre': 'shounen', 'release_year': 2005},
  {'title': 'Jujutsu Kaisen', 'creator': 'Gege Akutami', 'genre': 'shounen', 'release_year': 2020},
]



# Create your views here.


def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'about.html')

def anime_index(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'anime/index.html', { 'anime': anime})