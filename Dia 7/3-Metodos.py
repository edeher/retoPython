class Pajaro:
    # Atributos de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # Método de instancia
    def cantar(self):
        print('Pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pájaro ha volado {metros} metros')


piolin = Pajaro("amarillo", "canario")
piolin.cantar()  # Salida: Pio
piolin.volar(100)  # Salida: El pájaro ha volado 100 metros