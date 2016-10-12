#!/usr/bin/python
from microbit import *

def show(points):
	array = [[0 for i in range(5)] for i in range(5)]
	for point in points:
		array[point[0]][point[1]] = 9
	string = ':'.join(''.join(str(cell) for cell in row) for row in array)
	image = Image(string)
	display.show(image)

tilt = 40

while True:

	x = accelerometer.get_x()
	y = accelerometer.get_y()

	if x > 2*tilt:
		col = 4
	elif x > tilt:
		col = 3
	elif x < -2*tilt:
		col = 0
	elif x < -tilt:
		col = 1
	else:
		col = 2

	if y > 2*tilt:
		row = 4
	elif y > tilt:
		row = 3
	elif y < -2*tilt:
		row = 0
	elif y < -tilt:
		row = 1
	else:
		row = 2

	show([[row, col]])

