class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice Mu!")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice Ve!")


vaca1 = Vaca("Lola")
oveja1 = Oveja("Dolly")
vaca1.hablar()
oveja1.hablar()

print("-----Polimorfismo1-----")
animales = [vaca1, oveja1]
for animal in animales:
    animal.hablar()
print("-----Polimorfismo2-----")


def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)
animal_habla(oveja1)