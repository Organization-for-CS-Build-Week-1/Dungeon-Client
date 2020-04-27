import os
import requests
import json

main_url = 'https://dungeon-test0234.herokuapp.com'
# 'https://safe-reef-80226.herokuapp.com'
# 'http://127.0.0.1:5000'

def make_request(dir, params=None, headers=None):
    url = main_url + dir
    response = requests.request('GET', url, params=params, headers=headers)
    return response.json()

def init_request(Authorization):
    headers = {'Authorization':Authorization}
    return make_request('/api/adv/init', headers=headers)

def move_request(Authorization, direction):
    params =  {'direction':direction}
    headers = {'Authorization':Authorization}
    return make_request('/api/adv/move', params=params, headers=headers)

def save_request(Authorization):
    headers = {'Authorization':Authorization}
    return make_request('/api/debug/save', headers=headers)

def load_request(Authorization):
    headers = {'Authorization':Authorization}
    return make_request('/api/debug/load', headers=headers)

def check_request():
    url = main_url + '/api/check'
    response = requests.request('GET', url)

    return response.status_code

def make_post(dir, json=None, headers=None):
    url = main_url + dir
    response = requests.post(url=url, json=json, headers=headers)
    return response.json()

def login_request(username, password):
    params =  {'username':username, 'password':password}
    return make_post('/api/login', json=params)

def register_request(username, password1, password2):
    params =  {'username':username, 'password1':password1, 'password2':password2}
    return make_post('/api/registration', json=params)

def debug_request(Authorization):
    headers = {'Authorization':Authorization}
    return make_post('/api/debug', headers=headers)