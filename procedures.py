from request_functions import *

AUTH_FAIL_MESSAGE = "Authorization failure. Please restart."

def login_reg_procedure():
    login_option = ""

    while login_option not in ['l', 'r']:
      login_option = input("Whould you like to [L]og in or [R]egister?\n> ").lower()[0]

      if login_option == 'l':
        auth = login_procedure()
      elif login_option == 'r':
        auth = registration_procedure()
      else:
        print("Invalid request. Either log in or register.")

    return auth

def login_procedure():
    username = input("Please enter your user name: ")
    password = input("Please enter your password: ")

    response = login_request(username, password)

    if 'error' in response:
        print(response['error'])
        return login_procedure()

    return response['key']

def registration_procedure():
    username = input("Please enter your desired user name: ")
    password1 = input("Please enter your desired password: ")
    password2 = input("Please reenter your desired password: ")

    response = register_request(username, password1, password2)

    if 'error' in response:
        print(response['error'])
        return registration_procedure()

    return response['key']

def init_procedure(auth):
    response = init_request(auth)

    if 'error' in response:
        print(AUTH_FAIL_MESSAGE)
    else:
        print("Welcome to the world of [Lambda School MUD #16476]!")

        print("Current room:",response['title'])
        print(response['description'])

def move_procedure(auth, direction):
    response = move_request(auth, direction)
    
    if 'error' in response:
        if response['error'] == "Malformed auth header":
            print(AUTH_FAIL_MESSAGE)
        else:
            print(response['error'])
    else:
        print("Current room:",response['title'])
        print(response['description'])

def debug_procedure(auth):
    response = debug_request(auth)
    
    if 'error' in response:
        print("I didn't understand that.")
    else:
        option = input("What would you like to do, admin?")

        if option = "s":
            save_procedure(auth)
        elif option = "l":
            load_procedure(auth)

def save_procedure(auth):
    response = save_request(auth)

    if 'error' in response:
        if response['error'] == "Malformed auth header":
            print(AUTH_FAIL_MESSAGE)
        else:
            print(response['error'])
    else:
        print(response['str'])

def load_procedure(auth):
    response = load_request(auth)

    if 'error' in response:
        if response['error'] == "Malformed auth header":
            print(AUTH_FAIL_MESSAGE)
        else:
            print(response['error'])
    else:
        print(response['str'])
