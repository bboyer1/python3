#!/usr/bin/python3

import requests

class Dog():
    def __init__(self, dog_type):
        self.dog_type = dog_type

    def create_url(self):
        self.url = 'https://dog.ceo/api/breeds/{self.dog_type}/images/random'

    def get_dog(self):
        return requests.get(self.url)



if __name__ == "__main__":
    main()