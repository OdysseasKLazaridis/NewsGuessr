from django.shortcuts import render
from django.views.generic import ListView
from .models import Quiz

# Create your views here.
class HomeView(ListView):
    model = Quiz
    template_name = "quiz/index.html"

class GameView(ListView):
    model = Quiz
    template_name = "game/game.html"
    context_object_name = "quiz"