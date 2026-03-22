from django.shortcuts import render
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    cat_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    context = {
        'cat_count' : cat_count,
        'blog_count' : blog_count,
    }
    return render(request , 'dashboard.html', context)