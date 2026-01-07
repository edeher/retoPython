import bs4
import requests

url = 'https://www.escueladirecta.com/l/products'
params = {
    'sortKey': 'name',
    'sortDirection': 'asc',
    'page': 1,
    'courseCategory': 'Excel',
}
resultado = requests.get(url, params=params)
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
imagenes = sopa.select('img')[0]['src']
print(imagenes)
imagen_curso_1 = requests.get(imagenes)

f = open('mi_imagen.jpg', 'wb')
f.write(imagen_curso_1.content)
f.close()
