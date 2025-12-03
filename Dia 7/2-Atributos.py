class Pajaro:
    # Atributos de clase
    alas = True

    # Atributos de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro("azul", "Tucan")
print(mi_pajaro.color)  # Salida: azul
print(mi_pajaro.especie)  # Salida: Tucan
print(f'mi pajaro es un {mi_pajaro.especie} de color {mi_pajaro.color} ')
print(mi_pajaro.alas)  # Salida: True
print(Pajaro.alas)  # Salida: True