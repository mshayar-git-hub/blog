from django.shortcuts import redirect, render

from blogs.models import Blog, Category

# Create your views here.
def post_by_category(request , category_id):
    post = Blog.objects.filter(status='PUBLISHED', category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    context = {
        'post' : post,
        'category' : category
    }
    return render(request ,'post_by_category.html',context)