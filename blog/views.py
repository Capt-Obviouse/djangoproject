from django.shortcuts import render
from .models import Posts
from django.contrib.auth import logout
from django.conf import settings

# Create your views here.

def home(request):
    posts = Posts.objects.all().order_by('-id')[:2]

    context = {
        'title': 'Latest Post',
        'posts': posts,
        'home': 'active',
    }
    return render(request, 'blog/index.html', context)

def blog(request):
        posts = Posts.objects.all().order_by('-id')

        context = {
            'title': 'Latest Post',
            'posts': posts,
            'blog': 'active',
        }
        return render(request, 'blog/blog.html', context)

def chapter(request, page):
    #posts = Posts.objects.all()
    posts = Posts.objects.filter(page_number__page_number=page)

    context = {
    'posts': posts,
    'body': "body stuff",
    'google_maps_api_key': getattr(settings, 'GOOGLE_MAPS_API_KEY', ''),
    }

    return render(request, 'blog/ch{}.html'.format(page), context)
