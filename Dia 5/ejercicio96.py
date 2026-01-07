"""Crea una función llamada `invertir_palabra` que tome los caracteres de
una palabra y devuelva la palabra invertida en mayúsculas.

Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver
"NOHTYP".

Crea también la variable `palabra` con un string de ejemplo para pasarla
como argumento a la función.
"""
palabra = "python"


def invertir_palabra(palabra):
    return palabra[::-1].upper()
