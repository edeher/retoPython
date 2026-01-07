# Devuelve la posición de un elemento según el índice de inicio de la
# búsqueda dentro de un string.

mi_texto = "Esta es una prueba"
resultado = mi_texto[-4]
resultado2 = mi_texto.index("a", 5)
resultado3 = mi_texto.rindex("a", 5)
resultado4 = mi_texto.find("a")
print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
