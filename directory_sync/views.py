import os

import flask
import workos

from django.shortcuts import render


workos.api_key = os.getenv('WORKOS_API_KEY')
workos.base_api_url = 'http://localhost:7000/' if settings.DEBUG else workos.base_api_url
DIRECTORY = os.getenv('SCIM_ENDPOINT_ID')  # follow guide to get this


@app.route('/users')
def directory_users():
    users = workos.client.directory_sync.list_users(directory=DIRECTORY)
    return users  # may need to return JsonResponse


@app.route('/groups')
def directory_groups():
    groups = workos.client.directory_sync.list_groups(directory=DIRECTORY)
    return groups # may need to return JsonResponse
