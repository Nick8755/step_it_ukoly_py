file = 'file_02.txt'
user_input = input('Zadejte text pro ulozeni do souboru: ') # Uživatel zadá text, který chce uložit do souboru

def write(): # Funkce, která uloží text do souboru
    with open('file_02.txt', 'a', encoding='utf-8') as file:
        file.write(user_input + '\n')
        print(f"Text '{user_input}' byl uložen do souboru.")

def read(): # Funkce, která načte text ze souboru
    with open('file_02.txt', 'r', encoding='utf-8') as file:
        print(file.read())

write() # Zavolání funkce write()
read()  # Zavolání funkce read()