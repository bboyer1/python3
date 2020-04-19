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


def main():
	
	parser = argparse.ArgumentParser(description='The Dog pic script')

	parser.add_argument(
		'-n',
		'--num',
		dest='num',
		type=int,
		default=1,
		help='Number of dog pics'
	)

	parser.add_argument(
		'-t',
		'--threads',
		dest='threads',
		type=int,
		required=True,
		help="Number of threads to run"
	)
	args = parser.parse_args()

	dog_pictures(args.num)

	with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
		executor.submit(download_img, img_list)


if __name__ == "__main__":
	main()