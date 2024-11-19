#prace se soubory

'''def read():
    with open('soubor.txt', mode='r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
#read()

def write():
    with open('soubor.txt', mode='w', encoding='utf-8') as file:
        file.write('Hello from Python\n')
#write()

def append():
    with open('soubor.txt', mode='a', encoding='utf-8') as file:
        file.write('Hello from\n')

append()
'''

data = 'data.csv'
import csv
with open(data, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)

import pandas as pd
df = pd.read_csv(data, delimiter=';')
print(df)