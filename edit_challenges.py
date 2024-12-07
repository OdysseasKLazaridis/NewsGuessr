from redditrewind_app.quiz.models import Daily_Challenge, Quiz, Choice
from datetime import date
import django
import os
import random
# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'redditrewind_app.settings.local')
django.setup()
def create_challenge(quizzes, date=None):
    # Set default date to today if no date is provided
    if date is None:
        date = date.today()

    # Delete existing challenge for the given date
    Daily_Challenge.objects.filter(challenge_date=date).delete()

    # Create or update the challenge for the given date
    challenge, created = Daily_Challenge.objects.update_or_create(challenge_date=date)

    # Loop through quizzes and create quiz and choices
    for quiz in quizzes:
        # Create the quiz
        q = challenge.quiz_set.create(text=quiz['text'])
        
        # Shuffle the choices so that the order is random
        random.shuffle(quiz['choices'])

        # Create the choices for the quiz
        for choice in quiz['choices']:
            q.choice_set.create(name=choice['name'], mentions=choice['mentions'], is_correct=choice['is_correct'])

quizzes = [
    {
        'text': 'Which of the following curse words was most frequently mentioned on Reddit this week?',
        'choices': [
            {'name': 'F*ck', 'mentions': 1200, 'is_correct': True},
            {'name': 'Sh*t', 'mentions': 900, 'is_correct': False},
            {'name': 'D*mn', 'mentions': 700, 'is_correct': False},
            {'name': 'B*tch', 'mentions': 500, 'is_correct': False}
        ]
    },
    {
        'text': 'Which subreddit mentioned the word "pizza" the most this week?',
        'choices': [
            {'name': 'r/FoodPorn', 'mentions': 850, 'is_correct': True},
            {'name': 'r/AskReddit', 'mentions': 600, 'is_correct': False},
            {'name': 'r/Pizza', 'mentions': 750, 'is_correct': False},
            {'name': 'r/food', 'mentions': 500, 'is_correct': False}
        ]
    },
    {
        'text': 'Which meme format was most used across Reddit this week?',
        'choices': [
            {'name': 'Distracted Boyfriend', 'mentions': 1500, 'is_correct': True},
            {'name': 'Mocking SpongeBob', 'mentions': 1200, 'is_correct': False},
            {'name': 'Two Buttons', 'mentions': 1000, 'is_correct': False},
            {'name': 'Woman Yelling at a Cat', 'mentions': 800, 'is_correct': False}
        ]
    },
    {
        'text': 'Which of the following topics had the most posts related to it on Reddit this week?',
        'choices': [
            {'name': 'AI and Machine Learning', 'mentions': 2000, 'is_correct': True},
            {'name': 'Cryptocurrency', 'mentions': 1800, 'is_correct': False},
            {'name': 'Space Exploration', 'mentions': 1500, 'is_correct': False},
            {'name': 'Climate Change', 'mentions': 1200, 'is_correct': False}
        ]
    },
    {
        'text': 'Which of these phrases was used the most in Reddit posts this week?',
        'choices': [
            {'name': 'No cap', 'mentions': 2200, 'is_correct': True},
            {'name': 'Bet', 'mentions': 1800, 'is_correct': False},
            {'name': 'FOMO', 'mentions': 1500, 'is_correct': False},
            {'name': 'I’m dead', 'mentions': 1300, 'is_correct': False}
        ]
    },
    {
        'text': 'Which movie or show had the most discussions this week on Reddit?',
        'choices': [
            {'name': 'The Last of Us', 'mentions': 3000, 'is_correct': True},
            {'name': 'House of the Dragon', 'mentions': 2200, 'is_correct': False},
            {'name': 'Breaking Bad', 'mentions': 1800, 'is_correct': False},
            {'name': 'Stranger Things', 'mentions': 1500, 'is_correct': False}
        ]
    },
    {
        'text': 'Which word was mentioned most in discussions about technology this week?',
        'choices': [
            {'name': 'AI', 'mentions': 2500, 'is_correct': True},
            {'name': 'Quantum Computing', 'mentions': 1800, 'is_correct': False},
            {'name': 'Bitcoin', 'mentions': 2200, 'is_correct': False},
            {'name': 'Electric Vehicles', 'mentions': 1700, 'is_correct': False}
        ]
    },
    {
        'text': 'Which word was mentioned the most in Reddit posts about "memes" this week?',
        'choices': [
            {'name': 'Dank', 'mentions': 2500, 'is_correct': True},
            {'name': 'Funny', 'mentions': 2100, 'is_correct': False},
            {'name': 'Meme', 'mentions': 1800, 'is_correct': False},
            {'name': 'LOL', 'mentions': 1500, 'is_correct': False}
        ]
    },
    {
        'text': 'Which emoji was used the most in Reddit posts this week?',
        'choices': [
            {'name': '😂', 'mentions': 3500, 'is_correct': True},
            {'name': '🔥', 'mentions': 2500, 'is_correct': False},
            {'name': '😎', 'mentions': 2000, 'is_correct': False},
            {'name': '🤯', 'mentions': 1500, 'is_correct': False}
        ]
    },
    {
        'text': 'Which video game had the most discussions on Reddit this week?',
        'choices': [
            {'name': 'Elden Ring', 'mentions': 2800, 'is_correct': True},
            {'name': 'Minecraft', 'mentions': 2500, 'is_correct': False},
            {'name': 'Fortnite', 'mentions': 2200, 'is_correct': False},
            {'name': 'Call of Duty', 'mentions': 2000, 'is_correct': False}
        ]
    }
]



create_challenge(date=date.today(), quizzes=quizzes)

