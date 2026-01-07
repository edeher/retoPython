import bs4
import requests

# crear URL sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 ó 5 estrellas

titulos_rating_alto = []

# Iterar Paginas

for pagina in range(1, 51):

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # Iterar libros
    for libro in libros:
        # chequear 4 ó 5 estrellas
        len1 = len(libro.select('.star-rating.Four'))
        len2 = len(libro.select('.star-rating.Five'))
        if (len1 != 0 or len2 != 0):
            # guardar titulo
            titulo_libro = libro.select('a')[1]['title']
            # agregar a la lista
            titulos_rating_alto.append(titulo_libro)
# ver libros
for t in titulos_rating_alto:
    print(t)
