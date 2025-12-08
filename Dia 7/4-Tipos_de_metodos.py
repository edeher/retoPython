class Pajaro:

    alas = True

    # Atributos de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # Métodos de instancia, necesta instanciar un objeto
    def cantar(self):
        print('Pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pájaro ha volado {metros} metros')
        self.cantar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"ahora el pajaro es {self.color}")

    # Metodo de class
    @classmethod
    def poner_huevos(cls, cantidad):
        cls.alas = False
        print(f'El pájaro ha puesto {cantidad} huevos')
        print(f'¿El pájaro tiene alas? {cls.alas}')

    # Metodo estatico
    @staticmethod
    def mirar():
        print("El pajaro mira")


piolin = Pajaro("amarillo", "canario")
piolin.pintar_negro()
piolin.volar(40)

Pajaro.poner_huevos(3)
Pajaro.mirar()