def lista_atributos(**kwargs):
    lista = []
    for clave, valor in kwargs.items():
        lista.append(valor)
    return lista


print(lista_atributos(x=1, y=2, z=3))