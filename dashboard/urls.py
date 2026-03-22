from django.conf import settings
from . import views
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from blogs import views as Blogsviews

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('dashboard_category/',views.dashboard_category,name='dashboard_category'),
    path('dashboard_category/dashboard_add_category',views.dashboard_add_category,name='dashboard_add_category'),
    path('dashboard_category/dashboard_edit_category/<int:pk>/',views.dashboard_edit_category,name='dashboard_edit_category'),
    path('dashboard_category/dashboard_delete_category/<int:pk>/',views.dashboard_delete_category,name='dashboard_delete_category')
]