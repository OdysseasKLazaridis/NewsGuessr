from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from .models import Daily_Challenge, Quiz, Choice
from datetime import date
from django.http import JsonResponse

# Create your views here.
class HomeView(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch today's challenge
        today = date.today()
        todays_challenge = Daily_Challenge.objects.filter(challenge_date=today).first()

        # Add context to check if there's a challenge for today
        context['has_challenge'] = bool(todays_challenge)  # True if there's a challenge, False if not
        return context


def game(request):
    # Fetch today's Daily Challenge
    today = date.today()
    print(today) 
    todays_challenge = Daily_Challenge.objects.filter(challenge_date=today).first()

    # Ensure the object exists and is passed to the template
    if todays_challenge:
        quizzes = list(todays_challenge.quiz_set.all())

        # Find the latest answered quiz based on cookies
        answered_quiz_ids = [
            int(key.split('_')[1]) for key in request.COOKIES.keys() 
            if key.startswith('quiz_') and request.COOKIES[key]
        ]
        
        # Find the next quiz that hasn't been answered yet
        next_quiz = next((quiz for quiz in quizzes if quiz.id not in answered_quiz_ids), None)

        if next_quiz:
            # If there are still unanswered quizzes, render the next quiz
            context = {'todays_challenge': todays_challenge}
        else:
            # If all quizzes have been answered, show a message
            context = {'message': 'You have completed the challenge!'}
            return render(request, 'game/game.html', context)
    else:
           
        return redirect('index')  # Redirect to the homepage or a custom 'no challenge' page

    print(todays_challenge)
    return render(request, 'game/game.html', context)



def submit_choices(request):
    today = date.today()
    todays_challenge = Daily_Challenge.objects.filter(challenge_date=today).first()
    quizzes = list(todays_challenge.quiz_set.all())
    for quiz in quizzes:
        print(quiz.id)
        cookie_name = "quiz_" + str(quiz.id)
        choice_id = request.COOKIES.get(cookie_name)
        choice = Choice.objects.get(id=choice_id)
        choice.add_one()
    return


def finished(request):
    context = {'message': 'You have completed the challenge!'}
    return render(request, 'game/finished.html', context)
