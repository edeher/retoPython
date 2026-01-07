import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')
print(resultado.text)
sopa = bs4.BeautifulSoup(resultado.text, "lxml")
print(sopa.select('h3.post-title.entry-title'))
print('-----------------------------------')
print(sopa.select('title'))
print('-----------------------------------')
print(len(sopa.select('p')))
print('-----------------------------------')
print(sopa.select('title')[0])
print('-----------------------------------')
print(sopa.select('title')[0].getText())
print('-----------------------------------')

# Parrafo especial
parrafo_especial = sopa.select('div')
# lista con muchos parrafos
print(parrafo_especial)
print('-----------------------------------')
# parrafo con indice
parrafo_especial = sopa.select('div')[3]
print(parrafo_especial)
print('-----------------------------------')
# parrafor con ubicacion y sin etiquetas
parrafo_especial = sopa.select('div')[3].getText()
print(parrafo_especial)
print('-----------------------------------')

columna_lateral = sopa.select('.sidebar p')
print(columna_lateral)
print('-----------------------------------fin')

for p in columna_lateral:
    print(p.getText())