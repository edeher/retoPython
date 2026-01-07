# Colecciones mutables que almacenan pares clave-valor. Cada clave es única
# y se usa para acceder a su valor asociado.
# Se definen con llaves `{}`; los pares se separan por dos puntos y los
# elementos por comas.
# Las claves deben ser inmutables (p. ej., cadenas o números); los valores
# pueden ser de cualquier tipo. Pueden contener listas.

mi_dic = {"c1": "valor1", "c2": "valor2", "c3": "valor3"}
print(type(mi_dic))
print(mi_dic)

resultado = mi_dic["c1"]
print(resultado)

cliente = {"nombre": "Juan", "apellido": "Fuentes", "peso": 88, "Talla": "1.76"}
cosnulta1 = cliente["apellido"]
print(cosnulta1)

dic = {"c1": 55, "c2": [10, 20, 30], "c3": {"s1": 100, "s2": 200}}
print(dic["c2"][1])
print(dic["c3"]["s2"])

dic2 = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
resultado2 = dic2["c2"][1]
print(resultado2.upper())

dic3 = {1: "a", 2: "b"}
print(dic3)

# agrega elementos
dic3[3] = "c"
print(dic3)

# modifica el valor
dic3[2] = "B"
print(dic3)

# devuelve las claves
print(dic3.keys())

# devuelve los valores
print(dic3.values())

# devuelve los elementos del diccionario como si fuera una lista
print(dic3.items())
