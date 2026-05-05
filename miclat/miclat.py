from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
import requests

from getpass import getpass
from django.conf import settings

from main import settings


def login():
    auth_endpoint = settings.MICLAT_AUTH_URL 
    auth_response = requests.post(auth_endpoint, json={"username": settings.MICLAT_USERNAME,"password": settings.MICLAT_PASSWORD}, verify=False) 

    if auth_response.status_code == 200:
        token = auth_response.json()['token']
        key = 'Bearer'
        headers = {
            "Authorization": f"{key} {token}"
        }
        return headers
    return -1

def get_data(nin):
    headers = login()
    if headers != -1:
        endpoint = f"{settings.MICLAT_API_URL}/{nin}/"
        get_response = requests.get(endpoint, headers=headers, verify=False) 
        return get_response
    else:
        return -1

# data = get_data('109920887131810000')
# print(data.json())
