from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required

from dashboard.forms import CategoryForm

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