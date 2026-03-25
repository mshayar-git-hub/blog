from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from blogs.models import Blog, Category, Comments

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

def single_blog(request ,slug):
    post = get_object_or_404(Blog, slug=slug)
    comments = Comments.objects.filter(blog = post)
    if request.method == 'POST':
        comment = Comments()
        comment.user = request.user
        comment.blog = post
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
    context = {
        'post' : post,
        'comments':comments,
    }
    return render(request, 'single_blog.html' , context)

def search_keyword(request):
    post_key = request.GET.get('keyword')
    post = Blog.objects.filter(Q(title__icontains = post_key) | Q(short_description__icontains = post_key) | Q(blog_body__icontains = post_key)  , status= 'PUBLISHED'  ).first()
    context = {
        'post' : post
    }
    return render(request, 'single_blog.html' , context)
    