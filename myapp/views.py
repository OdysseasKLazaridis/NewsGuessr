from django.shortcuts import render
from .models import Question
from .models import BlogPost 
def home(request):
    posts = BlogPost.objects.all()

    list_of_values = []
    list_of_values.append("first entry")
    list_of_values.append("second entry")
    context= {}


    questions = Question.objects.all()
    context['questions'] = questions
    #context = {}
    #context['some_string']="this is some string that I'm passing to the view"
    return render(request, 'myapp/index.html', context)

def test(request):
    posts = BlogPost.objects.all()

    list_of_values = []
    list_of_values.append("first entry")
    list_of_values.append("second entry")
    context= {}


    questions = Question.objects.all()
    context['questions'] = questions
    #context = {}
    #context['some_string']="this is some string that I'm passing to the view"
    return render(request, 'myapp/test.html', context)

