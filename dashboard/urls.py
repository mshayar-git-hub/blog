from django.conf import settings
from . import views
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from blogs import views as Blogsviews

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    # category
    path('dashboard_category/',views.dashboard_category,name='dashboard_category'),
    path('dashboard_category/dashboard_add_category',views.dashboard_add_category,name='dashboard_add_category'),
    path('dashboard_category/dashboard_edit_category/<int:pk>/',views.dashboard_edit_category,name='dashboard_edit_category'),
    path('dashboard_category/dashboard_delete_category/<int:pk>/',views.dashboard_delete_category,name='dashboard_delete_category'),
    #post
    path('dash_post/',views.dash_post,name='dash_post'),
    path('post/dash_add_post',views.dash_add_post,name='dash_add_post'),
    path('post/dash_edit_post/<int:pk>/',views.dash_edit_post,name='dash_edit_post'),
    path('post/dash_delete_post/<int:pk>/',views.dash_delete_post,name='dash_delete_post'),
    #Users
    path('users/',views.users,name='users'),
    path('add_user/',views.add_user,name='add_user'),
    path('edit_user/<int:pk>',views.edit_user,name='edit_user'),
    path('delete_user/<int:pk>',views.delete_user,name='delete_user'),
    #logout
    path('dash_logout/',views.dash_logout,name='dash_logout'),
]