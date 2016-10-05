#!/usr/bin/python
from microbit import *

start_time = running_time()

def show(points):
	array = [[0 for i in range(5)] for i in range(5)]
	for point in points:
		array[point[0]][point[1]] = 9
	string = ':'.join(''.join(str(cell) for cell in row) for row in array)
	image = Image(string)
	display.show(image)

row = 4
col = 2

while True:

	a = button_a.get_presses()
	b = button_b.get_presses()

	if(a > 0 and col > 0):
		col -= 1

	if(b > 0 and col < 4):
		col += 1

	show([[row, col]])
	sleep(10)





