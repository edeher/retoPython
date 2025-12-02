# mi_archivo = open('prueba.txt')
# toda_lineas = mi_archivo.read()
# print(toda_lineas)
# print('--------------------------------------------')
# print('-------------------------')
# una_linea = mi_archivo.readline()
# print(una_linea.rstrip())
# print('-------------------------')
# una_linea = mi_archivo.readline()
# print(una_linea.rstrip())
# print('-------------------------')
# una_linea = mi_archivo.readline()
# print(una_linea)


# print('--------------------------------------------')

# for l1 in mi_archivo:
#     print("Aqui dice :"+l1)
# mi_archivo.close()

# print('--------------------------------------------')
# todas = mi_archivo.readlines()
# # todas = todas.pop()
# print(todas)

mi_archivo = open('prueba.txt')
cont = 0
for l1 in mi_archivo:
    if cont == 1:
        print('la segunda linea es : '+l1)
    cont += 1