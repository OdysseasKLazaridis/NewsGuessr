
from django.urls import  path
from . import views
urlpatterns = [
    path("", views.HomeView.as_view(), name = "index"),
    path('game.html', views.game, name='game'),
    path('next-quiz/<int:quiz_id>/', views.next_quiz, name='next_quiz'),
    

]