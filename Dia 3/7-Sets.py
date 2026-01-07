# Colección de elementos únicos y no ordenados. La duplicidad no está
# permitida y el orden no importa. Son útiles para operaciones de conjuntos
# como la unión, intersección y diferencia. Los elementos deben ser
# inmutables.
# aunque el conjunto en sí es mutable y puede ser modificado.
# de definen set([]) , set(()) y {}

mi_set = set([1, 2, 3, 4, 5, 6])

print(type(mi_set))
print(mi_set)

mi_set2 = set((1, 2, 3, 4, 5))
print(type(mi_set2))
print(mi_set2)

otro_set = {1, 2, 3, 4, (1, 2, 3), 5, 1, 1, 2, 2, 2}
print(type(otro_set))
print(otro_set)

print(len(otro_set))
print(2 in otro_set)

# se peude unir dos Sets
s3 = mi_set.union(mi_set2)
print(s3)

# agregar elementos
s3.add(7)

# eleiminar elementos
s3.remove(3)

# descartar elmentos
s3.discard(4)

# elimina un elmento aleatoriamente
s3.pop()
print(s3)

# limpia el set
s3.clear()
print(s3)
