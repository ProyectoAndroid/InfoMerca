import urllib2
from bs4 import BeautifulSoup

linkPrincipal = "http://www.linio.com.pe/tv-audio-y-video/televisores/?page=1"

content = urllib2.urlopen(linkPrincipal).read()

freeShiping = False

soup = BeautifulSoup(content)
for paquete in soup.find_all("ul", id="catalog-items"):

    resultado = BeautifulSoup(str(paquete))

    for marca in resultado.find_all("li"):
            if marca["class"] == ["product-item-brand"]:
                print marca.string.lstrip()


























