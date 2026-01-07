# extr una porcion de texto indicando :
# cadena[inicio:fin]: Extrae caracteres desde el índice inicio hasta uno antes del índice fin.
# cadena[:fin]: Obtiene caracteres desde el principio de la cadena hasta uno antes de fin.
# cadena[inicio:]: Obtiene caracteres desde inicio hasta el final de la cadena.
# cadena[:]: Crea una copia de la cadena completa.
# cadena[5:10:2] # obtiene caracteres desde el índice 5 hasta el 10
# (excluido), tomando cada 2 caracteres
mi_variable = "esta palabra sera extraida"
palabra = "palabra"
resultado = mi_variable[5:12]
resultado2 = mi_variable[5:]
resultado3 = mi_variable[:5]
resultado4 = mi_variable[0:10:2]
resultado5 = mi_variable[::-1]
resultado6 = palabra[::-1].upper()
print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
