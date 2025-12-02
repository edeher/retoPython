archivo = open("prueba.txt", "w")

archivo.write("soy el nuevo texto\n")
archivo.write('''
hola
soy el nuevo texto
escribeme''')
print('-----------------------------------')
archivo.writelines(['Hello', 'Word', 'here', 'I', 'am'])
lista = ['Hello', 'Word', 'here', 'I', 'am']

for l1 in lista:
    archivo.write(l1+'\n')

print('-----------------------------------')

archivo = open("prueba.txt", "a")

archivo.write('bienvenido1')

archivo.close()
