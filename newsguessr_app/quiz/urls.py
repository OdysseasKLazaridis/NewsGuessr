
from django.urls import  path
from . import views
urlpatterns = [
    path("", views.HomeView.as_view(), name = "homepage"),
    path("game.html", views.GameView.as_view(), name = "game"),
]