

from .models import About, Category, Follow_link


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_about_us(request):
    about_us = About.objects.first()
    return dict(about_us = about_us)

def get_follow_link(request):
    follow_link = Follow_link.objects.all()
    return dict(follow_link = follow_link)