from django.urls import path
from django.views.generic import RedirectView

from account import views

urlpatterns = [
    # path('games/', GameDetails.as_view(), name="games"),
    # path('games/<int:game_id>', GameDetails.as_view()),
    path('register', views.register, name='register'),
    path('redirect-to-register-page', RedirectView.as_view(url='http://localhost:3333/register'), name='redirect-to-register-page'),
    path('successful-registered', RedirectView.as_view(url='http://localhost:3333/games/minecraft'), name='successful-registered'),
    # path('games/<int:game_id>/additions/', GameDetails.as_view(), name="games/additions"),
    # path('home', views.home, name="home-page"),
    # path('add', views.add, name="add-page"),
    # path('delete', views.delete, name="delete-page"),
    # path('edit', views.edit, name="edit-page"),
    # path('find', views.find, name="find-page"),
    # path('show', views.show, name="show-page"),
    # path('games/', GamesList.as_view()),
    # path('games/<int:game_id>', GameDetails.as_view())
]