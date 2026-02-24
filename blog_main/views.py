from django.shortcuts import render

from blogs.models import Blog, Category


def home(request):
    featured_post = Blog.objects.filter(is_featured = True)
    post = Blog.objects.filter(is_featured=False , status = 'PUBLISHED')
    context = {
        'featured_post' : featured_post,
        'post' : post,
    }
    return render (request , 'index.html' , context)