#!/usr/bin/python
from microbit import *
from random import *

def line(row1, col1, row2, col2):
	points = []
	m = (0.01 + col2 - col1) / (0.01 + row2 - row1)
	b = col1 - m * row1
	for row in range(min(row1,row2), max(row1,row2)+1):
		col = int(round(m * row + b))
		if col in range(5): points += [[row, col]]
	for col in range(min(col1,col2), max(col1,col2)+1):
		row = int(round((col - b)/m))
		if row in range(5): points += [[row, col]]
	return points

def show(points):
	array = [[0 for i in range(5)] for i in range(5)]
	for point in points:
		array[point[0]][point[1]] = 9
	string = ':'.join(''.join(str(cell) for cell in row) for row in array)
	image = Image(string)
	display.show(image)

speed = 100
while True:
	for col in range(2,5):
		show(line(2, 2, 0, col))
		sleep(speed)
	for row in range(1,5):
		show(line(2, 2, row, 4))
		sleep(speed)
	for col in range(3,0,-1):
		show(line(2, 2, 4, col))
		sleep(speed)
	for row in range(4,0,-1):
		show(line(2, 2, row, 0))
		sleep(speed)
	for col in range(0,1):
		show(line(2, 2, 0, col))
		sleep(speed)

