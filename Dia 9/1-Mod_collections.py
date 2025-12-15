from collections import Counter, defaultdict, namedtuple, deque
numeros = [8, 6, 9, 5, 4, 5, 5, 8, 7, 4, 5, 4, 4]
print(Counter(numeros)) 

print(Counter("mississippi"))

frase = 'al pan pan y al vino vino'

print(Counter(frase.split()))

serie = Counter([1, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5])
print(serie.most_common(1))
print(serie.most_common(3))
print(list(serie))
# Conta a frequência de cada número na lista
print('-----------------------------------')


mi_dic = {'uno': 'verde', 'dos': 'azul', 'tres': 'rojo'}
print(mi_dic['dos']) 

mi_dic1 = defaultdict(lambda: 'nada')
mi_dic1['uno'] = 'verde'
print(mi_dic1['dos'])
print(mi_dic1)

print('-----------------------------------')
mi_tupla = (500, 18, 65)
print(mi_tupla[1])

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])

ariel = Persona('Ariel', 180, 75)

print(ariel.nombre)
print(ariel.altura)
print(ariel.peso)
print(ariel)
print('-----------------------------------')