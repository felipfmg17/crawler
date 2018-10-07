import requests
import http.client
from bs4 import BeautifulSoup

def testRequests():
	r = requests.get('https://google.com')
	text = r.text
	with open('google.html','w') as f:
		f.write(text)
	f.close()


def testTitles():
	headers = {'User-Agent': 'Chrome/39.0.2171.95'}
	url = 'https://gameplanet.com/catalogo/video-juegos/software.html?dir=desc&mostrar_inventario=652&order=popularidad&p=1&plataforma=667'
	r = requests.get(url, headers=headers)
	text = r.text
	print(text)


def downloadHTTP(url):
	headers = {'User-Agent': 'Chrome/39.0.2171.95'}
	r = requests.get(url, headers=headers)
	text = r.text
	#print(text)
	return text

url = 'https://gameplanet-53f8.kxcdn.com/media/catalog/product/cache/4/small_image/228x/9df78eab33525d08d6e5fb8d27136e95/f/i/fifa_19_ps4_1.jpg' 


def downloadResource(host,resource):
    headers = {'User-Agent': 'Mozilla/5.0'}
    conn = http.client.HTTPSConnection(host)
    conn.request('GET',resource,'',headers)
    response = conn.getresponse()
    data = response.read()
    return data

def downloadResource2(host,resource, heads):
    headers = {'User-Agent': 'Mozilla/5.0'}
    heads.update(heads)
    conn = http.client.HTTPSConnection(host)
    conn.request('GET',resource,'',headers)
    response = conn.getresponse()
    data = response.read()
    return data




def saveToFile(data, file_name):
	print('saving data')
	with open(file_name, 'wb') as f:
		f.write(data)
	f.close()

	
def downloadImage():
	host = 'gameplanet-53f8.kxcdn.com'
	resource = '/media/catalog/product/cache/4/small_image/228x/9df78eab33525d08d6e5fb8d27136e95/f/i/fifa_19_ps4_1.jpg'
	text = downloadResource(host, resource)
	saveToFile(text,'fifa.jpg')

def downloadGamePlanet():
	host = 'gameplanet.com'
	resource = '/'
	text = downloadResource(host, resource)
	print(text)


def downloadGamePlanet2():
	cookie = '''sucuri_cloudproxy_uuid_46d59f0fa=d2c2ea4eb070a5e259777e265406626d;path=/;max-age=86400'''
	heads = {'Cookie': cookie }
	host = 'gameplanet.com'
	resource = '/'
	text = downloadResource2(host, resource, heads)
	print(text)


downloadGamePlanet2()
