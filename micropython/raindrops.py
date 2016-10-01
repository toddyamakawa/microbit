#!/usr/bin/python
from microbit import *
from random import *

def array2string(array):
	return ':'.join(''.join(str(cell) for cell in row) for row in array)

def drop(array):
	new_array = array[0:-1]
	new_row = [value-5 if value-5>0 else 0 for value in array[0]]
	new_row[randint(0,4)] = randint(0,9)
	new_array.insert(0, new_row)
	return new_array

array = [[0 for i in range(5)] for i in range(5)]

while True:
	array = drop(array)
	string =  array2string(array)
	image = Image(string)
	display.show(image)
	sleep(100)

