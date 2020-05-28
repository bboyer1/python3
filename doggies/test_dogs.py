import pytest

from dogs import Dog

class TestDog():
    def test_create_url(self):
        dog = Dog('Beagle')
        assert Equal(dog.create_url, f'https://dog.ceo/api/breeds/{self.dog_type}/images/random')