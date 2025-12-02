def suma(**kwargs):
    print(type(kwargs))


suma(x=3, y=5, z=2)

print("-------------------------")


def suma1(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}={valor}")


suma1(x=3, y=5, z=2)


print("-------------------------")


def suma2(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave}={valor}")
        total += valor
    return total


resultado = suma2(x=3, y=5, z=2)
print(resultado)
print("-------------------------")


def suma3(num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    for arg in args:
        print(f"args = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave}={valor}")


suma3(5, 6, 100, 200, 300, 400, 500, x=3, y=5, z=2)
print("-------------------------")


def suma4(num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    for arg in args:
        print(f"args = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave}={valor}")


args = [100, 200, 300, 400]
kwargs = {"x": "uno", "y": "dos", "z": "tres"}

suma4(5, 6, *args, **kwargs)
