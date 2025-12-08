class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal ha nacido")

    def hablar(self):
        print("El animal hace un sonido")


class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pájaro está volando {metros} metros")


class Felino(Animal):
    def __init__(self, edad, color, raza):
        super().__init__(edad, color)
        self.raza = raza


# piolin = Pajaro(3, "amarillo", 60)
# piolin.nacer()
# piolin.hablar()
# piolin.volar(100)

print("-------------------------------")


class Padre:
    def hablar(self):
        print("Hola")


class Madre():
    def reir(self):
        print("jejejejejejeje")

    def hablar(self):
        print("Que tal")


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
print(Nieto.__mro__)
print(Nieto.mro())