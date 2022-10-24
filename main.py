from os import system
import requests


system('cls')
print('=' * 40)
print('|', '--- INFORCAR ---'.center(36), '|')
print('=' * 40)
marca = str(input('Qual marca deseja consultar?: ')).lower()


try:
    r = requests.get(f'http://localhost:5000/carros/{marca}')
    data = r.json()

    
    print(f'mostrando todos carros da marca: {marca}')
    for c in data['carros']:
        print(f'- {c}')
except:
    print('Não foi possivel localizar está marca!')