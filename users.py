
import os, json

DATA_PATH1 = 'C:/Users/Nikita Abramenko/step_it/test_git_repo/users.json'
DATA_PATH2 = 'users.json'


def read_data():
    with open(DATA_PATH1, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_data(data):
    with open(DATA_PATH1, 'w', encoding='utf-8') as file:
        json.dump(data, file)
        

def check_password(password, password_repeat):
    if password != password_repeat:
        raise ValueError('Passwords do not match!')

def register(username, password, password_repeat):
    check_password(password, password_repeat)
    data = read_data()

    if username in data:
        raise ValueError('User already exists!')
    
    data[username] = password
    write_data(data)



def login(username, password):
    pass


def logout(username):
    pass

def change_password(password, new_password, new_password_repeat):
    pass

register('milan', 'heslo3', 'heslo3')