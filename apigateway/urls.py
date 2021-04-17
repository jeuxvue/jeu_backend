from django.urls import path
from .views import *


urlpatterns = [
    # path('games/', GameDetails.as_view(), name="games"),
    path('games/<int:game_id>', GameDetails.as_view()),
    path('creator-roles', CreatorRoles.as_view()),
    path('creators', CreatorsList.as_view()),
    path('creators/<int:creator_id>', CreatorDetails.as_view()),
    path('developers', DevelopersList.as_view()),
    path('developers/<int:developer_id>', DeveloperDetails.as_view()),
    path('games', GamesList.as_view()),
    path('games/<int:game_id>', GameDetails.as_view()),
    path('games/<int:game_id>/additions', GameAdditions.as_view()),
    # path('developers/page/<int:page_number>', DevelopersListWithPagination.as_view()),
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
