precios_cafe = [('capuchino', 1.5), ('expreso', 3.2), ('latte', 1.8),
                ('moca', 2.0)]
for elemento in precios_cafe:
    print(elemento)
print('------------------------------')
for elemento in precios_cafe:
    print(f'El precio del {elemento[0]} es {elemento[1]} euros.')
print('------------------------------')
for cafe, precio in precios_cafe:
    print(cafe)
print('------------------------------')
for cafe, precio in precios_cafe:
    print(precio*0.25)

print('------------------------------')


def cafe_mas_caro(lista_precios):
    cafe_mas_caro = ''
    precio_mayor = 0
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
    return cafe_mas_caro, precio_mayor


cafe, precio = cafe_mas_caro(precios_cafe)
lista_2 = cafe_mas_caro(precios_cafe)
print(f'El café más caro es {cafe} y cuesta {precio} euros.')
print(lista_2)