def describir_persona(nombre, **kwargs):
    print(f"caracteristicas de {nombre} :")
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")


describir_persona('Edeher', ojos='azules', talla='180cm', hobby='video juegos')