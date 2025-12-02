def describir_persona(nombre, **kwargs):
    print(f"caracteristicas de {nombre} :")
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")