from django.urls import path
from . import views
from .views import GamesList, GameDetails


urlpatterns = [
    # path('', views.home, name="home-page"),
    # path('home', views.home, name="home-page"),
    # path('add', views.add, name="add-page"),
    # path('delete', views.delete, name="delete-page"),
    # path('edit', views.edit, name="edit-page"),
    # path('find', views.find, name="find-page"),
    # path('show', views.show, name="show-page"),
    path('games/', GamesList.as_view()),
    path('game/<int:game_id>', GameDetails.as_view())
]
