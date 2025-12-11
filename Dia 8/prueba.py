def mi_generador():
    numero = 3
    while (numero > 0):
        yield print(f"Te quedan {numero} vidas")
        numero = numero - 1
    print("Game Over")


perder_vida = mi_generador()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))