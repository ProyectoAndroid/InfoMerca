import urllib2
from bs4 import BeautifulSoup

url = "http://www.linio.com.pe/tv-audio-y-video/televisores/televisores/?sort=price&dir=asc"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

for nombre_producto in soup.find_all("em"):
    print nombre_producto.string.lstrip()