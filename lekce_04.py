from users import login, register
while True:
    username = input('Zadejte username: ')
    password = input('Zadejte heslo: ')
    success = login(username, password)
    if success:
        print('OK')
        break