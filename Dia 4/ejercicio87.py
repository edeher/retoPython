"""Para realizar el ejercicio que sigue, puedes optar por varios caminos.
Aunque diferentes aproximaciones son válidas, te animo a practicar
comprensiones de listas para afianzar el concepto.

Convierte la lista de temperaturas en Fahrenheit a Celsius usando la
fórmula:

°C = (°F - 32) * (5/9)

La lista es:

temperatura_fahrenheit = [32, 212, 275]

Almacena el resultado en la variable `grados_celsius`.
"""
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(n - 32) * (5 / 9) for n in temperatura_fahrenheit]
