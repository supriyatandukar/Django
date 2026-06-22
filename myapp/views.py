from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

def hello_world(request):
    return HttpResponse("<h1>Hello, Django!</h1>")

def home(request):
    context = {
        'title': 'Welcome to Django Workshop',
        'message': 'Your first Django app!',
        'features': ['Fast', 'Secure', 'Scalable', 'Easy'],
        'year': 2026
    }
    return render(request, 'myapp/home.html', context)

def about(request):
    return render(request, 'myapp/about.html', {'title': 'About Us'})

def contact(request):
    return render(request, 'myapp/contact.html', {'title': 'Contact Us', 'email': 'info@company.com'})

def questions(request):
    from .models import Question, Choice

    question_list = Question.objects.all()
    choice_list = Choice.objects.all()
    return render(request, 'myapp/questions.html', {'questions': question_list, 'choices': choice_list, 'title': 'Questions List'})

def vote(request, question_id, choice_id):
    from .models import Choice

    choice = get_object_or_404(Choice, pk=choice_id, question_id=question_id)
    choice.votes += 1
    choice.save()
    return redirect('questions')
   