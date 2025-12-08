class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("El animal ha nacido")


class Pajaro(Animal):
    pass


print(Pajaro.__bases__)
print(Animal.__subclasses__())

print("--------------------")
piolin = Pajaro(22, "amarillo")
piolin.nacer()
print(piolin.color)
print(piolin.edad)

