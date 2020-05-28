import pytest

from dogs import Dog

class TestDog():
    #@classmethod
    def setUp(self):
        self.dog = Dog('Beagle')

    def test_create_url(self):
        assert Equal(self.dog.url, f'https://dog.ceo/api/breeds/{self.dog_type}/images/random')