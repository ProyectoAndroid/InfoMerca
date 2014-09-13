import urllib2
from bs4 import BeautifulSoup

url = "http://www.linio.com.pe/tv-audio-y-video/televisores/televisores/?sort=price&dir=asc"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)
for paquete in soup.find_all("ul", id="catalog-items"):
    #print nombre_producto.string.lstrip()
    #if nombre_producto.get('title') is not None:
    #    print nombre_producto.get('title')
    resultado = BeautifulSoup(str(paquete))

    for nombre_resultado in resultado.find_all("a"):
        print nombre_resultado['title']