from django.conf import settings
from . import views
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from blogs import views as Blogsviews

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
]