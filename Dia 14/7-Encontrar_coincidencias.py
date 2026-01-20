import cv2
import face_recognition as fr
import os
import numpy

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

# tomar una imagen de camara web
captura =cv2.VideoCapture(0, cv2.CAP_DSHOW)

# leer la imagen de la cara
exito, imagen = captura.read()

if not exito:
    print("no se pudo capturar")
else:
    # reconocer cara en captura
    cara_captura = fr.face_locations(imagen)

    # codificar cara capturada

    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # buscar coincidencias
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        cincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)
        print(distancias)

        indice_coincidencia = numpy.argmin(distancias)

        # mostrar coincidencias
        if distancias[indice_coincidencia] > 0.6:
            print(" no coincide con alguien")
        else:
            print("Bienvenido al trabajo")

