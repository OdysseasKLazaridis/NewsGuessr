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
    },
    {
        'text': 'What is the meaning of life?',
        'choices': [
            {'name': '42', 'mentions': 100, 'is_correct': True},
            {'name': 'Eat pizza and nap', 'mentions': 5, 'is_correct': False},
            {'name': 'To get more memes', 'mentions': 3, 'is_correct': False},
            {'name': 'Have a pet rock', 'mentions': 2, 'is_correct': False}
        ]
    },
    {
        'text': 'What is the best meme of all time?',
        'choices': [
            {'name': 'Distracted Boyfriend', 'mentions': 50, 'is_correct': True},
            {'name': 'Grumpy Cat', 'mentions': 40, 'is_correct': False},
            {'name': 'Doge', 'mentions': 30, 'is_correct': False},
            {'name': 'Kermit Sipping Tea', 'mentions': 20, 'is_correct': False}
        ]
    },
    {
        'text': 'What do you do when you see a dog?',
        'choices': [
            {'name': 'Pet it and say "good dog"', 'mentions': 70, 'is_correct': True},
            {'name': 'Ignore it', 'mentions': 5, 'is_correct': False},
            {'name': 'Yell "doggo!" and run away', 'mentions': 3, 'is_correct': False},
            {'name': 'Give it a meme', 'mentions': 20, 'is_correct': False}
        ]
    },
    {
        'text': 'What’s the best way to procrastinate?',
        'choices': [
            {'name': 'Watch cat videos', 'mentions': 100, 'is_correct': True},
            {'name': 'Take a nap', 'mentions': 40, 'is_correct': False},
            {'name': 'Stare at your screen pretending to work', 'mentions': 50, 'is_correct': False},
            {'name': 'Start a new project you’ll never finish', 'mentions': 10, 'is_correct': False}
        ]
    },
    {
        'text': 'What would you rather do?',
        'choices': [
            {'name': 'Have unlimited tacos', 'mentions': 80, 'is_correct': True},
            {'name': 'Get free WiFi forever', 'mentions': 40, 'is_correct': False},
            {'name': 'Be a professional meme creator', 'mentions': 20, 'is_correct': False},
            {'name': 'Binge-watch Netflix for a day', 'mentions': 30, 'is_correct': False}
        ]
    },
    {
        'text': 'What is the ultimate breakfast food?',
        'choices': [
            {'name': 'Pancakes with syrup', 'mentions': 90, 'is_correct': True},
            {'name': 'Bacon', 'mentions': 70, 'is_correct': False},
            {'name': 'Avocado toast', 'mentions': 50, 'is_correct': False},
            {'name': 'Cereal with milk', 'mentions': 40, 'is_correct': False}
        ]
    },
    {
        'text': 'What’s the real secret to success?',
        'choices': [
            {'name': 'Hard work and dedication', 'mentions': 60, 'is_correct': False},
            {'name': 'Memes and coffee', 'mentions': 80, 'is_correct': True},
            {'name': 'Pretend to know what you’re doing', 'mentions': 20, 'is_correct': False},
            {'name': 'Bribing your way to the top', 'mentions': 30, 'is_correct': False}
        ]
    },
    {
        'text': 'What do you do when you’re bored?',
        'choices': [
            {'name': 'Scroll through TikTok', 'mentions': 80, 'is_correct': True},
            {'name': 'Solve a Rubik’s Cube', 'mentions': 20, 'is_correct': False},
            {'name': 'Play an online game', 'mentions': 50, 'is_correct': False},
            {'name': 'Take a nap', 'mentions': 10, 'is_correct': False}
        ]
    }
]


create_challenge(date=date.today(), quizzes=quizzes)

