from random import randint


def lanzar_dados():
    return randint(1, 6), randint(1, 6)


def evaluar_jugada(dado1, dado2):
    suma = dado1 + dado2
    if suma <= 6:
        print(f"La suma de tus dados es {suma}. Lamentable")
    elif 6 < suma < 10:
        print(f"La suma de tus dados es {suma}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma}. Parece una jugada ganadora")


dado1, dado2 = lanzar_dados()
print(dado1, dado2)
evaluar_jugada(dado1, dado2)