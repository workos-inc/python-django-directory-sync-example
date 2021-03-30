from django.urls import path
from . import views

urlpatterns = [
    path('users', views.get_directory_users, name='users'),
    path('groups', views.get_directory_groups, name='groups'),
]
