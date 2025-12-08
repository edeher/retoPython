mi_lista = [1, 1, 1, 1, 1, 1, 1]
print(len(mi_lista))


class Objeto:
    pass


mi_objeto = Objeto()
print(mi_objeto)

print("----------------------")


class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"{self.titulo} de {self.autor}, {self.canciones} canciones"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("El CD ha sido eliminado")


mi_cd = CD("Pink Floyd", "The Wall", 24)
print(mi_cd)
print(len(mi_cd))

del mi_cd