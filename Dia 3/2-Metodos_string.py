texto = "Este es el texto de Federico"
# convierte el texto a Mayuscula
resultado = texto.upper()

# convirte el texto a miniscula
resultado2 = texto.lower()

# divide el texto en una lista de subcadenas usando los espacios en blanco
resultado3 = texto.split()

# divide el texto en una lista de subcadenas usando loa letra "t"
resultado4 = texto.split("t")

a = "Aprender"
b = "Python"
c = "es"
d = "genial"

# Concatena elementos de una lista o tupla en una sola cadena
e = " ".join([a, b, c, d])

# busca la priemra ocurrencia de una subcadena y devuelve el indice
resultado5 = texto.find("s")

# reemplaza texto una subcadena por otra
resultado6 = texto.replace("s", "p")

print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(e)
print(resultado5)
print(resultado6)
