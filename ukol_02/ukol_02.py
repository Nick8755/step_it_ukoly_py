file = 'file_02.txt'
user_input = input('Zadejte text pro ulozeni do souboru: ')

def write():
    with open('file_02.txt', 'a', encoding='utf-8') as file:
        file.write(user_input + '\n')
        print(f"Text '{user_input}' byl uložen do souboru.")

def read():
    with open('file_02.txt', 'r', encoding='utf-8') as file:
        print(file.read())

write()
read()