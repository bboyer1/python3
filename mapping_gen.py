#!/usr/bin/python3

def house_price_and_int(cost):
    cost *= 1.03
    return cost

def random_price(size):
    import random
    randomlist = random.sample(range(100_000, 500_000), size)
    return randomlist


myList = random_price(10)
print(list(map(house_price_and_int, myList)))
