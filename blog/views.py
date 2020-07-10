from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Ibraj khan',
        'title': 'Blog Post 1',
        'content': 'The life change',
        'date_of_post': 'June 6 , 2020'
    },

    {
        'author': 'Mumtaz khan',
        'title': 'Blog Post 2',
        'content': 'HTML5',
        'date_of_post': 'June 10 , 2020'
    }
]


def home(request):
    return render(request, 'blog/home.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


