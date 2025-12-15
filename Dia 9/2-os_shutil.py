import os
# import shutil
# import send2trash

print(os.getcwd())

archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir())

# shutil.move('curso.txt', "C:\\Users\\yosoy\\OneDrive\\Desktop")

# eliminar

# send2trash.send2trash('curso.txt')

print(os.walk("C:\\Users\\yosoy\\OneDrive\\Desktop"))

ruta = 'C:\\Users\\yosoy\\OneDrive\\Documentos\\Projetcs Python'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'en la carpeta : {carpeta}')
    print('las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')

