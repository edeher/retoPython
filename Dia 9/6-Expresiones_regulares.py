import re

texto1 = '''si necesitas ayuda llama al (658)-598-9977
las 24 horas al servicio de ayuda online'''

patron1 = 'nada'
patron2 = 'ayuda'

busqueda = re.search(patron1, texto1)
busqueda2 = re.search(patron2, texto1)
busqueda3 = re.findall(patron2, texto1)

print(busqueda)
print(busqueda2)
print(busqueda2.span())
print(busqueda2.start())
print(busqueda2.end())
print(busqueda3)
print(len(busqueda3))

for hallazgo in re.finditer(patron2, texto1):
    print(hallazgo.span())
print('----------------------------------------------------')
texto2 = 'llama al 564-525-6588 ya mismo'

patron1 = r'\d\d\d-\d\d\d-\d\d\d\d'
patron2 = r'\d{3}-\d{3}-\d{4}'
patron3 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado1 = re.search(patron1, texto2)
resultado2 = re.search(patron2, texto2)
resultado3 = re.search(patron3, texto2)
print(resultado1)
print(resultado1.group())
print(resultado2.group())
print(resultado3.group(1))
print(resultado3.group(2))
print(resultado3.group(3))
print('----------------------------------------------------')
# clave = input("clave :")
# patron4 = r'\D{1}\w{7}'
# chequear = re.search(patron4, clave)
# print(chequear)
print('----------------------------------------------------')

texto3 = 'no atendemos los lunes por la tarde'
buscar1 = re.search(r'lunes|martes', texto3)
buscar2 = re.search(r'..demos', texto3)
# busca algo al comienzo
buscar3 = re.search(r'^\D', texto3)
# busca algo al final
buscar4 = re.search(r'\D$', texto3)
# excluir
buscar5 = re.findall(r'[^\s]', texto3)
buscar6 = re.findall(r'[^\s]+', texto3)

print(buscar1)
print(buscar2)
print(buscar3)
print(buscar4)
print(buscar5)
print(buscar6)

texto4 = 'edercin@gmail.com.br'
buscar7 = re.search(r'@\w+\.com', texto4)
print(buscar7)
