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
