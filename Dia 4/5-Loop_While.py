respuesta ='s'
while respuesta == 's':
    respuesta =input("quieres seguir? (s/n)")
else:
    print("Gracias")
print("--------------------------------------------------")
nombre=input("dime tu nombre: ")
for letra in nombre:
    if letra=='e':
        pass
    print(letra)
print("--------------------------------------------------")
for letra in nombre:
    if letra == 'e':
        break
    print(letra)
print("--------------------------------------------------")
for letra in nombre:
    if letra=='e':
        continue
    print(letra)