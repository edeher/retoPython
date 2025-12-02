def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus numeros es {suma_numeros}"
    
    
resultado = numeros_persona('edeher', 2, 3, 4, 5, 6, 11)
print(resultado)