from django.urls import path

from myapp import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello_world, name='hello'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('questions/', views.questions, name='questions'),
    path('vote/<int:question_id>/<int:choice_id>/', views.vote, name='vote'),
]