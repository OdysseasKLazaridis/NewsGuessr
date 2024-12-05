from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Daily_Challenge, Quiz
from datetime import date
from django.http import JsonResponse

# Create your views here.
class HomeView(ListView):
    model = Quiz
    template_name = "quiz/index.html"

def game(request):
    from datetime import date

    # Fetch today's Daily Challenge
    today = date.today()
    todays_challenge = Daily_Challenge.objects.filter(challenge_date=today).first()

    # Ensure the object exists and is passed to the template
    if todays_challenge:
        first_quiz = todays_challenge.quiz_set.first()  # Fetch the first quiz
        context = {'quiz': first_quiz}

    else:
        context = {'error': 'No challenge found for today!'}

    return render(request, 'game/game.html', context)


def next_quiz(request, quiz_id):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Fetch today's challenge
        today = date.today()
        todays_challenge = Daily_Challenge.objects.filter(challenge_date=today).first()
        
        if not todays_challenge:
            return JsonResponse({'success': False, 'message': 'No Daily Challenge available for today.'})

        # Find the next quiz
        quizzes = list(todays_challenge.quiz_set.all())
        current_quiz_index = next((i for i, q in enumerate(quizzes) if q.id == int(quiz_id)), -1)
        
        if current_quiz_index == -1 or current_quiz_index + 1 >= len(quizzes):
            return JsonResponse({'success': False, 'message': 'No more quizzes available.'})
        
        next_quiz = quizzes[current_quiz_index + 1]

        # Render the next quiz to HTML
        context = {'quiz': next_quiz}
        html = render(request, 'game/quiz_fragment.html', context).content.decode('utf-8')

        return JsonResponse({'success': True, 'html': html})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})
