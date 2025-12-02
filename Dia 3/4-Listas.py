# colección de elementos ordenados y modificables
# se definen usando corchetes `` y separando los elementos con comas.

mi_lista = ["a", "b", "c"]
mi_lista2 = ["d", "e", "f"]
mi_lista3 = mi_lista + mi_lista2
otra_lista = ["hola", 55, 6.1]
resultado = len(mi_lista)

# trae el contendo de la ubicacion especifiada
resultado2 = mi_lista[1]

# trae la lista en segun lo indicado
resultado3 = mi_lista[0:2]

print(mi_lista)
print(otra_lista)
print(resultado)
print("resultado2: " + resultado2)
print(resultado3)
print(mi_lista + mi_lista2)
print(mi_lista3)

# modifica el contenido segun la ubicacion
mi_lista3[0] = "alfa"
print(mi_lista3)

# Agrega un nuevo elemento a la lista
mi_lista3.append("gama")
print(mi_lista3)

# elemina por defecto el ultimo elemento
mi_lista3.pop()
print(mi_lista3)

# elemina el elemento segundo ubicacion del elemento
mi_lista3.pop(0)
print(mi_lista3)

# guarda el elemento extraido
eliminado = mi_lista3.pop(0)
print(eliminado)

print(mi_lista3)


lista = ["g", "o", "b", "m", "c"]

# ordena la lista en forma ascedente
lista.sort()
print(lista)

# Invierte el orden de ua lista
lista.reverse()
print(lista)
