import urllib2
from bs4 import BeautifulSoup

cantidad = 1

linkPrincipal = "http://www.linio.com.pe/"

categorias = ("tv-audio-y-video", "computadoras", "camaras", "videojuegos", "celulares-telefonia-y-gps")

subcategorias = [["televisores", "accesorios-para-tv", "reproductores-de-video", "cine-en-casa"],
                 ["laptops-y-notebooks", "desktops", "apple", "tablets-y-accesorios", "gamers"],
                 ["digitales", "profesionales", "videocamaras"], ["preventas", "playstation", "nintendo", "xbox-360"],
                 ["celulares-iphones", "celulares", "accesorios-para-celulares", "gps"]]

for categoria in range(categorias.__len__()):

    for subcategoria in range(subcategorias[categoria].__len__()):

        for numeroPagina in range(cantidad):

            url = linkPrincipal + categorias[categoria] + "/" + subcategorias[categoria][subcategoria] + "/?page=" + str(numeroPagina)

            content = urllib2.urlopen(url).read()

            soup = BeautifulSoup(content)
            for paquete in soup.find_all("ul", id="catalog-items"):

                resultado = BeautifulSoup(str(paquete))

                for nombre_resultado in resultado.find_all("a"):
                    print nombre_resultado['title']

                for imagen in resultado.find_all("img"):
                    if imagen["src"].find("https://") != -1:
                        print imagen["src"]

                for precioOld in resultado.find_all("span"):
                    if precioOld["class"] == ["product-itm-price-old"]:
                        print precioOld.string

                for precioNew in resultado.find_all("span"):
                    if precioNew["class"] == ["product-itm-price-new"]:
                        print precioNew.string

