import zipfile
import shutil

# comprimir archivos

mi_zip = zipfile.ZipFile("archivo_comprimido.zip", "w")
mi_zip.write("mi_texto_A.txt")
mi_zip.write("mi_texto_B.txt")
mi_zip.close()
print('--------------------------------------------')
# Descompromir archivos

zip_abierto = zipfile.ZipFile("archivo_comprimido.zip", "r")
zip_abierto.extractall()
print('--------------------------------------------')
carpeta_origen = "C:\\Users\\yosoy\\OneDrive\\Desktop\\secuencias"

archivo_destino = 'Todo_comprimido'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

print('--------------------------------------------')
shutil.unpack_archive('Todo_comprimido.zip', 'Extraccion Terminada', 'zip')