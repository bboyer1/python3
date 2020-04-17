#!/usr/bin/python3


import requests
import json
import threading

img_list=[]

def download_img(url_list):

	for url in url_list:
		img = requests.get(url).content
		img_name = url.split('/')[4]
		img_name = f'{img_name}.jpg'

		with open(img_name, 'wb') as img_file:
			img_file.write(img)
			print(f'{img_name} was downloaded' )


def dog_pictures(volume):
	response = requests.get(f'https://dog.ceo/api/breeds/image/random/{volume}')
	images = response.json()['message']

	for i in images:
		img_list.append(i)
	return img_list

t1 = threading.Thread(target=dog_pictures, args=(50,))
t2 = threading.Thread(target=dog_pictures, args=(50,))

t1.start()
t2.start()

t1.join()
t2.join()

download_img(img_list)