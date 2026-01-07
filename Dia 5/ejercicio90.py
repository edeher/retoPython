"""Verifica si los sets a continuación forman conjuntos aislados (es decir,
que no tienen elementos en común) utilizando el método `isdisjoint()`.
Almacena el resultado en la variable `conjuntos_aislados`.

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

Consulta la documentación del método para entender su funcionamiento.
"""
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
if marcas_smartphones.isdisjoint(marcas_tv):
    print("no tienen elementos en comun")
else:
    conjuntos_aislados = False
