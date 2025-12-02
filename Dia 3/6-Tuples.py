# colección ordenada e inmutable de elementos, lo que significa que una vez creada no se puede modificar su contenido.
# Se definen con paréntesis ().
# comienza con indice [0]
mi_tuple = (1, 2, 3, 4)
mi_tuple2 = (5, 5.6, "a")
mituple3 = (1, 2, (10, 20), 4)
mi_tuple = list(mi_tuple)

# puedes agrega un tupa al mismo numero de variables iguales
w, x, y, z = mi_tuple


print(type(mi_tuple))
print(mi_tuple)

# devuelve el elemento segun idice
print(mi_tuple2[0])

# devuelve el elemento segun idice y subindice
print(mituple3[2][1])
print(w, x, y, z)
t = (1, 2, 3, 1)

# cuenta cuantas veces aparece un elemento
print(t.count(1))

# devuelve el indece de un elemento
print(t.index(2))
