import os
import requests
import json

main_url = 'http://127.0.0.1:5000'

def make_request(dir, params=None, headers=None):
    url = main_url + dir
    response = requests.request('GET', url, params=params, headers=headers)
    return response.json()

def register_request(username, password1, password2):
    params =  {'username':username, 'password1':password1, 'password2':password2}
    return make_request('/api/registration/', params=params)

def login_request(username, password):
    params =  {'username':username, 'password':password}
    return make_request('/api/login/', params=params)

def init_request(Authorization):
    headers = {'Authorization':Authorization}
    return make_request('/api/adv/init/', headers=headers)

def move_request(Authorization, direction):
    params =  {'direction':direction}
    headers = {'Authorization':Authorization}
    return make_request('/api/adv/move/', params=params, headers=headers)

def debug_request(Authorization):
    headers = {'Authorization':Authorization}
    return make_request('/api/debug/', headers=headers)

def save_request(Authorization):
    headers = {'Authorization':Authorization}
    return make_request('/api/save/', headers=headers)

def load_request(Authorization):
    headers = {'Authorization':Authorization}
    return make_request('/api/load/', headers=headers)
