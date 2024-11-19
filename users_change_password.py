# users_change_password.py

import os, json, hashlib

DATA_PATH = 'users.json'

def hash_password(password):
    hash_value = hashlib.sha256(password.encode()).hexdigest()
    return hash_value

def read_data():
    with open(DATA_PATH, encoding='utf-8') as file:
        return json.load(file)

def write_data(data):
    with open(DATA_PATH, mode="w", encoding='utf-8') as file:
        json.dump(data, file) # zapís do json

def check_password(password, password_repeat):
    if password != password_repeat:
        raise ValueError('Passwords do not match')

def check_username(data, username):
    if username in data:
        raise ValueError('User already exists')

def register(username, password, password_repeat):
    check_password(password, password_repeat)
    data = read_data()
    check_username(data, username)
    data[username] = hash_password(password)
    write_data(data)

def login(username, password):
    data = read_data()
    try:
        assert data[username] == password, 'Password is incorrect'
        return True
    except (KeyError, AssertionError):
        return False
#Tady je cast ukolu (change_password) !!!!!!
def change_password(username, old_password, password, password_repeat):
    data = read_data()
    if username not in data:
        raise ValueError('User does not exist')
    if data[username] != old_password:
        raise ValueError('Old password is incorrect')

    check_password(password, password_repeat)
    data[username] = password
    write_data(data)


def delete_user(username, password):
    data = read_data()
    if username in data and data[username] == password:
        del data[username]
        write_data(data)


#register('jarda', 'heslo5', 'heslo5')
#print value from hash code
#print(hash_password('heslo4'))
#delete_user('jana', 'heslo2')
#change_password('milan', 'heslo3', 'new_heslo', 'new_heslo')


