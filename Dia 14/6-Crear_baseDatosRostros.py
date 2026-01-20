import cv2
import face_recognition as fr

import os

# crear DB
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    image_actual = cv2.imread(f'{ruta}\{nombre}')
    mis_imagenes.append(image_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])
print(nombres_empleados)

# codificar imagenes
def codificar(imagenes):

    # crear lista nueva
    lista_codificada = []

    # pasar las imagenes a RGB
    for image in imagenes:
        imagen = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        #codificar
        codificado = fr.face_encodings(imagen)[0]

        # agregar a la lista
        lista_codificada.append(codificado)

    # devolver lista codificada
    return lista_codificada

lista_empleados_codificada = codificar(mis_imagenes)
print(len(lista_empleados_codificada))