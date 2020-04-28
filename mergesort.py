#!/usr/bin/python3

def create_array(size=100, max=1000):
    from random import randint
    return [randint(0,max) for i in range(size)]

def merge(a_list, b_list):
    myList = []
    left_index, right_index= 0, 0

    while left_index<len(a_list) and right_index<len(b_list):
        if a_list[left_index]<b_list[right_index]:
            myList.append(a_list[left_index])
            left_index+=1
        else:
            myList.append(b_list[right_index])
            right_index+=1

    if left_index==len(a):
        myList.extend(b_list[right_index:])
    else:
        myList.extend(a_list[left_index:])
    return myList

def merge_sort(a):
    if len(a)<=1:
        return a
    left = merge_sort(a[:len(a)//2])
    right = merge_sort(a[len(a)//2:])
    return merge(left, right)

a = create_array()
print(a)
s=merge_sort(a)
print(s)
