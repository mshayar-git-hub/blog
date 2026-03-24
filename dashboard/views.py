from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib.auth.models import User

from dashboard.forms import AddUserForm, BlogForm, CategoryForm, EditUserForm

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    cat_count = Category.objects.all().count()
    blog_count = Blog.objects.all().count()
    context = {
        'cat_count' : cat_count,
        'blog_count' : blog_count,
    }
    return render(request , 'dashboard/dashboard.html', context)

@login_required(login_url='login')
def dashboard_category(request):
        return render(request, 'dashboard/dashboard_category.html')

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
      return render(request, 'dashboard/dashboard_add_category.html' , context)

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
      return render(request, 'dashboard/dashboard_edit_category.html', context)

@login_required(login_url='login')
def dashboard_delete_category(request, pk):
      category = get_object_or_404(Category, pk=pk)
      category.delete()
      return redirect('dashboard_category')


#post
@login_required(login_url='login')
def dash_post(request):
    post = Blog.objects.all()
    context={
          'post':post,
    }
    return render(request, 'dashboard/dash_post.html', context)

@login_required(login_url='login')
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
      return render(request, 'dashboard/dash_add_post.html', context)

@login_required(login_url='login')
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
    return render(request , 'dashboard/dash_edit_post.html' , context)

@login_required(login_url='login')
def dash_delete_post(request , pk):
    temp_post = get_object_or_404(Blog,pk=pk)
    temp_post.delete()
    return redirect('dash_post')

@login_required(login_url='login')
def users(request):
    users = User.objects.all()
    context={
        'users':users,
    }
    return render (request,'dashboard/users.html',context)

@login_required(login_url='login')
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form = AddUserForm()
    context ={
        'form' : form,
    }
    return render(request,'dashboard/add_user.html',context)

def edit_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    form = EditUserForm(instance=user)
    context = {
        'user':user,
        'form':form
    }
    return render(request , 'dashboard/edit_user.html',context)

def delete_user(request,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')