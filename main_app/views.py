from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Anime, Character
from .forms import EpisodeForm


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
  anime = Anime.objects.all()
  return render(request, 'anime/index.html', { 'anime': anime})

def anime_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    id_list = anime.characters.all().values_list('id')
    characters_anime_doesnt_have = Character.objects.exclude(id__in=id_list)
    episode_form = EpisodeForm()
    return render(request, 'anime/detail.html', {
      'anime': anime, 'episode_form': episode_form,
      'characters': characters_anime_doesnt_have
      })

def assoc_character(request, anime_id, character_id):
    # Note that you can pass a toy's id instead of the whole toy object
    Anime.objects.get(id=anime_id).characters.add(character_id)
    return redirect('detail', anime_id=anime_id)

def remove_character(request, anime_id, character_id):
    # Note that you can pass a toy's id instead of the whole toy object
    Anime.objects.get(id=anime_id).characters.remove(character_id)
    return redirect('detail', anime_id=anime_id)

def add_episode(request, anime_id):
 # create a ModelForm instance using the data in request.POST
  form = EpisodeForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_episode = form.save(commit=False)
    new_episode.anime_id = anime_id
    new_episode.save()
  return redirect('detail', anime_id=anime_id)

class AnimeCreate(CreateView):
  model = Anime
  fields = ['title', 'creator', 'genre', 'release_year']

class AnimeUpdate(UpdateView):
  model = Anime
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['creator', 'genre', 'release_year']

class AnimeDelete(DeleteView):
  model = Anime
  success_url = '/anime'

class CharacterList(ListView):
  model = Character

class CharacterDetail(DetailView):
  model = Character

class CharacterCreate(CreateView):
  model = Character
  fields = '__all__'

class CharacterUpdate(UpdateView):
  model = Character
  fields = ['name', 'color']

class CharacterDelete(DeleteView):
  model = Character
  success_url = '/characters'