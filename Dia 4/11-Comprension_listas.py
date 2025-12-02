palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

print('-------------------------------')

lista1 = [letra for letra in palabra]
print(lista1)

print('-------------------------------')

lista2 = [letra for letra in 'palabras']
print(lista2)

print('-------------------------------')

lista3 = [n for n in range(0, 20, 2)]
print(lista3)

print('-------------------------------')

lista4 = [n/2 for n in range(0, 20, 2)]
print(lista4)

print('-------------------------------')

lista5 = [n for n in range(0, 20, 2) if n*2 > 10]
print(lista5)

print('-------------------------------')

lista6 = [n if n*2 > 10 else 'no'for n in range(0, 20, 2)]
print(lista6)
print('-------------------------------')
pies = [10, 20, 30, 40, 50]


metros = [n*3.281 for n in pies]
print(metros)