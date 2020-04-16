from request_functions import *

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
        print("Authorization failure.")
        return

    print("Welcome to the world of [Lambda School MUD #16476]!")

    print("Current room:",response['title'])
    print(response['description'])

def move_procedure(auth, direction):
    response = move_request(direction, auth)
    
    if 'error' in response:
        if response['error'] == "Malformed auth header":
            print("Authorization failure.")
            return
        else:
            print(response['error'])
    else:
        print("Current room:",response['title'])
        print(response['description'])
