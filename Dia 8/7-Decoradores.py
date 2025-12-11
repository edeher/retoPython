def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())
    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula


operacion = cambiar_letras("may")
operacion("Hola Mundo")  # Output: HOLA MUNDO
print("----------------------------------------")


def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adiós")
    return otra_funcion


# @decorar_saludo
# def mayuscula(texto):
#     print(texto.upper())


# @decorar_saludo
# def miniscula(texto):
#     print(texto.lower())


# mayuscula("Python")
# miniscula("Python")
print("----------------------------------------")


def mayuscula(texto):
    print(texto.upper())


def miniscula(texto):
    print(texto.lower())


mayuscula_Decorada = decorar_saludo(mayuscula)
mayuscula('fede')
mayuscula_Decorada('fede')

