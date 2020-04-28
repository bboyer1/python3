#!/usr/bin/python3


def addit(n):
    return n+n

hello = (1,2,3,4)

result = map(addit, hello)

print(dir(result)
print(list(result))
