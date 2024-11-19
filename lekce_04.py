import hashlib

text = 'ohcoqgcoweg'
hash = hashlib.sha256(text.encode()).hexdigest()


from ukol_01_users_change_password import login, register
while True:
    username = input('Zadejte username: ')
    password = input('Zadejte heslo: ')
    success = login(username, password)
    if success:
        print('OK')
        break
    else:
        print('Chyba')