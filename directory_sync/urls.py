from django.urls import path
from . import views

urlpatterns = [
    path('/users', views.directory_users, name='users'),
    path('/groups', views.directory_groups, name='groups'),
]
