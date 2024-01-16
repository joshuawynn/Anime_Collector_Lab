from django.db import models
from django.urls import reverse
from datetime import date

RATINGS = (
    ('B', 'Bad'),
    ('G', 'Good'),
    ('A', 'Awesome')
)

# Create your models here.

class Character(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('characters_detail', kwargs={'pk': self.id})

class Anime(models.Model):
    title = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    genre = models.TextField(max_length=250)
    release_year=models.IntegerField()
    characters = models.ManyToManyField(Character)

    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'anime_id': self.id})
    
class Episode(models.Model):
  date = models.DateField('episode date')
  rating = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=RATINGS,

    default=RATINGS[0][0]
  )
  
  anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
  
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_rating_display()} on {self.date}"

  class Meta:
    ordering = ['-date']