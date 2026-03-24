from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from dashboard.forms import BlogForm, CategoryForm

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

@login_required(login_url='login')
def dashboard_category(request):
        return render(request, 'dashboard_category.html')

@login_required(login_url='login')
def dashboard_add_category(request):
      if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid:
                  form.save()
                  return redirect('dashboard')
      form = CategoryForm()
      context = {
            'form' : form
      }
      return render(request, 'dashboard_add_category.html' , context)

@login_required(login_url='login')
def dashboard_edit_category(request , pk):
      category = get_object_or_404(Category, pk=pk)
      if request.method == 'POST':
            form = CategoryForm(request.POST ,instance = category)
            if form.is_valid:
                  form.save()
                  return redirect('dashboard_category')
      form = CategoryForm(instance = category)
      context = {
            'form':form,
            'category' : category,
      }
      return render(request, 'dashboard_edit_category.html', context)

@login_required(login_url='login')
def dashboard_delete_category(request, pk):
      category = get_object_or_404(Category, pk=pk)
      category.delete()
      return redirect('dashboard_category')


#post

def dash_post(request):
    post = Blog.objects.all()
    context={
          'post':post,
    }
    return render(request, 'dash_post.html', context)

def dash_add_post(request):
      if request.method == 'POST':
            form = BlogForm(request.POST , request.FILES)
            if form.is_valid():
                post1 = form.save(commit = False) #temprory save
                post1.author = request.user
                form.save()
                post1.slug = slugify(post1.title) + '-' +str(post1.id)
                form.save()
                return redirect('dash_post')
            else:
                print(form.errors)
      form = BlogForm()
      context = {
            'form' : form,
      }
      return render(request, 'dash_add_post.html', context)

def dash_edit_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES ,instance=post)
        if form.is_valid:
            post11 = form.save(commit = False)
            form.save()
            post11.slug = slugify(post11.title)+'-'+str(post11.id)
            form.save()
            return redirect('dash_post')
    form = BlogForm(instance=post)
    context = {
        'form' : form,
        'post':post,
    }
    return render(request , 'dash_edit_post.html' , context)

def dash_delete_post(request , pk):
    temp_post = get_object_or_404(Blog,pk=pk)
    temp_post.delete()
    return redirect('dash_post')