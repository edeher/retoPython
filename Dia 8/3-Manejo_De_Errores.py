def suma():
    try:
        n1 = int(input("Ingrese un número: "))
        n2 = int(input("Ingrese otro número: "))
        print(n1 + n2)
        print("Gracias por sumar")
        # print("Gracias por sumar"+ n1)
    except TypeError:
        print("Ha ocurrido un error. Estas concatenando string con number.")
    except ValueError:
        print("Ha ocurrido un error. Debes ingresar números válidos.")
    else:
        print("La suma se realizó correctamente.")
    finally:
        print("Fin del programa.")


def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
        except ValueError:
            print("Error: Debe ingresar un número válido.")
        else:
            print(f"Has ingresado el número: {numero}")
            break
    print("Gracias")


pedir_numero()


# try:
#     suma()
# except TypeError:
#     print("Ha ocurrido un error. Estas concatenando string con number.")
# except ValueError:
#     print("Ha ocurrido un error. Debes ingresar números válidos.")
# else:
#     print("La suma se realizó correctamente.")
# finally:
#     print("Fin del programa.")
