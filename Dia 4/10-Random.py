from random import randint, uniform, random, choice, shuffle

aleatorio = randint(1, 10)
print(aleatorio)

print('----------------------')

aleatorio1 = round(uniform(1, 10), 1)
print(aleatorio1)
print('----------------------')

aleatorio2 = random()
print(aleatorio2)
print('----------------------')

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio3 = choice(colores)
print(aleatorio3)

print('----------------------')

numeros = list(range(5, 50, 5))
print(numeros)
# este metodo no se peude almacenar
shuffle(numeros)
print(numeros)