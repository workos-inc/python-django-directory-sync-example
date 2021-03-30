import os

import workos

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render


workos.api_key = os.getenv('WORKOS_API_KEY')
workos.base_api_url = 'http://localhost:8000/' if settings.DEBUG else workos.base_api_url
directory_id = os.getenv('DIRECTORY_ID')  # Follow the WorkOS guide to get this


def get_directory_users(request):
    users = workos.client.directory_sync.list_users(directory=directory_id)
    print(users)
    return JsonResponse(data=users)


def get_directory_groups(request):
    groups = workos.client.directory_sync.list_groups(directory=directory_id)
    return JsonResponse(data=groups)
