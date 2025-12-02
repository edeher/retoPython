#enumerate() añade un contador a un iterable (como una lista o tupla)
# y lo devuelve en un objeto enumerate.
lista=['a','b','c']
indice=0
for letra in lista:
    print(f"Letra {indice}: {letra}")
    indice+=1
print("-------------------------------")
lista=['a','b','c']

for letra in enumerate(lista):
    print(f"Letra : {letra}")
    indice+=1
print("-------------------------------")
lista=['a','b','c']

for indice, letra in enumerate(lista):
    print(f"Letra {indice}: {letra}")
    indice+=1

print("-------------------------")
mis_tuples=list(enumerate(lista))
print(mis_tuples)

print("-------------------------")
mis_tuples=list(enumerate(lista))
print(mis_tuples[1])

print("-------------------------")
mis_tuples=list(enumerate(lista))
print(mis_tuples[1][0])