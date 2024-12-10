from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path('game.html', views.game, name='game'),
    path('finished', views.finished, name='finished'),  # This is correct
    path('submit_choices', views.submit_choices, name='submit_choices'),
]
