#!/usr/bin/python
from microbit import *
from random import *

def combine(array, string):
	return string.join(str(element) for element in array)

def array2image(array):
	return combine([combine(row,'') for row in array], ':')

def array2image2(array):
	dummy = []
	for row in array:
		dummy.append(combine(row, ''))
	return combine(dummy, ':')

while True:
	rand = [[randint(0,9) for i in range(5)] for i in range(5)]
	string =  array2image2(rand)
	image = Image(string)
	display.show(image)
	sleep(100)

