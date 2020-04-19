#!/usr/bin/python3

import argparse
import requests
import concurrent.futures

img_list = []

def download_img(url_list):
	"""Downloads all of the images into separate files"""
	for url in url_list:
		img = requests.get(url).content
		img_name = url.split('/')[4]
		img_name = f'{img_name}.jpg'

		with open(img_name, 'wb') as img_file:
			img_file.write(img)
			print(f'{img_name} was downloaded' )


def dog_pictures(volume):
	"""Builds the image list with urls"""
	response = requests.get(f'https://dog.ceo/api/breeds/image/random/{volume}')
	images = response.json()['message']

	for i in images:
		img_list.append(i)
	return img_list

dog_pictures(50)

with concurrent.futures.ThreadPoolExecutor() as executor:
	executor.submit(download_img, img_list)