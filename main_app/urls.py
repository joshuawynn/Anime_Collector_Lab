from django.urls import path
from . import views
	
urlpatterns = [
	 path('', views.home, name='home'),
      path('about/', views.about, name='about'),
      path('anime/', views.anime_index, name='index'),
      path('anime/<int:anime_id>', views.anime_detail, name='detail'),
      path('anime/create/', views.AnimeCreate.as_view(), name='anime_create'),
      path('anime/<int:pk>/update/', views.AnimeUpdate.as_view(), name='anime_update'),
      path('anime/<int:pk>/delete/', views.AnimeDelete.as_view(), name='anime_delete'), 
      path('anime/<int:anime_id>/add_episode/', views.add_episode, name='add_episode'),  
      path('characters/', views.CharacterList.as_view(), name='characters_index'),
      path('characters/<int:pk>/', views.CharacterDetail.as_view(), name='characters_detail'),
      path('characters/create/', views.CharacterCreate.as_view(), name='characters_create'),
      path('characters/<int:pk>/update/', views.CharacterUpdate.as_view(), name='characters_update'),
      path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='characters_delete'),
      path('characters/<int:anime_id>/assoc_character/<int:character_id>/', views.assoc_character, name='assoc_character'),
      path('characters/<int:anime_id>/remove_character/<int:character_id>/', views.remove_character, name='remove_character'),
 ]