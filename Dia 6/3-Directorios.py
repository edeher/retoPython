import os
from pathlib import Path
# # usanod chdir de os
ruta = os.chdir('/Users/deka/Documents/ProjectPython/project1/files')
archivo = open('otro_archivo.txt')
print(archivo.read())

print('---------------------------------------------------------------')
# Usando ruta absoluta
otro_archivo = open('/Users/deka/Documents/ProjectPython/project1/'
                    'files/otro_file.txt')
print(otro_archivo.read())

print('---------------------------------------------------------------')
# Crear directorios
ruta = os.makedirs('/Users/deka/Documents/ProjectPython/project1/files/otra')
# Eliminar directorios
os.rmdir('/Users/deka/Documents/ProjectPython/project1/files/otra')
print('---------------------------------------------------------------')
# # Usando Path
carpeta = Path('/Users/deka/Documents/ProjectPython/project1/files')
archivo2 = carpeta / 'otro_file.txt'
mi_archivo2 = open(archivo2)
print(mi_archivo2.read())
print('---------------------------------------------------------------')
# # usando Path segunda fomra
carpeta = (Path('/Users/deka/Documents/ProjectPython/project1/files') /
           'otro_file2.txt')

mi_archivo2 = open(carpeta)
print(mi_archivo2.read())


# # Propiedades de los directorios y archivos os
print('---------------------------------------------------------------')
ruta = '/Users/deka/Documents/ProjectPython/project1/Dia 6/prueba.txt'
elemento = os.path.basename(ruta)
print('basename : '+elemento)
elemento = os.path.dirname(ruta)
print('dirname : '+elemento)
elemento = os.path.split(ruta)
print('split : ', elemento)
elemento = os.path.exists(ruta)
print('exists : ', elemento)
elemento = os.path.isfile(ruta)
print('isfile : ', elemento)
elemento = os.path.isdir(ruta)
print('isdir : ', elemento)
elemento = os.path.splitext(ruta)
print('splitex : ', elemento)
