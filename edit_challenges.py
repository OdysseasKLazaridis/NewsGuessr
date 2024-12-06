from newsguessr_app.quiz.models import Daily_Challenge, Quiz, Choice
from datetime import date
import django
import os
# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsguessr_app.settings.local')
django.setup()
def create_challenge(quizzes, date = date.today):
    Daily_Challenge.objects.filter(challenge_date=date).delete()

    t, created = Daily_Challenge.objects.update_or_create(challenge_date=date)
    t.save()
    for quiz in quizzes:
        q = t.quiz_set.create(text=quiz['text']) 
        for choice in quiz['choices']:
            q.choice_set.create(name=choice['name'], mentions=choice['mentions'], is_correct=choice['is_correct'])

quizzes = [
    {
        'text': 'What is the capital of France?',
        'choices': [
            {'name': 'Paris', 'mentions': 10, 'is_correct': True},
            {'name': 'London', 'mentions': 5, 'is_correct': False},
            {'name': 'Berlin', 'mentions': 2, 'is_correct': False},
            {'name': 'Madrid', 'mentions': 3, 'is_correct': False}
        ]
    },
    {
        'text': 'Who is the president of the USA?',
        'choices': [
            {'name': 'Joe Biden', 'mentions': 15, 'is_correct': True},
            {'name': 'Donald Trump', 'mentions': 4, 'is_correct': False},
            {'name': 'Barack Obama', 'mentions': 6, 'is_correct': False},
            {'name': 'George Bush', 'mentions': 3, 'is_correct': False}
        ]
    }
]

create_challenge(date=date.today(), quizzes=quizzes)

