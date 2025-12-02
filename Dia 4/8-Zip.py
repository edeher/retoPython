nombres = [
    "Ana",
    "Hugo",
    "Valeria",
]
edades = [
    12,
    15,
    18,
]
ciudades = ["Lima", "Madrid", "Mexico"]

combinados = list(zip(nombres, edades, ciudades))

print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vivie en {ciudad}")
