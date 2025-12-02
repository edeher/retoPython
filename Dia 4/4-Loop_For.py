list=['a','b','c','d','e']

for letra in list:
    numero_letra=list.index(letra)+1
    print(f"Letra {numero_letra}: {letra}")
    #print("letra : "+letra)
print('---------------------------------------')
list2=['pablo','laura','fede','luis','julia','deka']
for nombre in list2:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print("nombre que no empieza por l:")

print('---------------------------------------')
numero=[1,2,3,4,5,6]
mi_valor=0
for number in numero:
    mi_valor=mi_valor+number
print(mi_valor)

print('---------------------------------------')
palabra='python'
for letra in palabra:
    print(letra)

print('---------------------------------------')

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

print('---------------------------------------')

dic={'clave1':'a','clave2':'b','clave3':'c'}
for item in dic.items():
    print(item)

for item in dic.values():
    print(item)

for a,b in dic.items():
    print(a,b)