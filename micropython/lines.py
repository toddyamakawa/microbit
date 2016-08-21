from microbit import *
from random import *

def line(x1, y1, x2, y2):
	points = []
	m = (0.0 + y2 - y1) / (0.0 + x2 - x1)
	b = y1 - m * x1
	for x in range(min(x1,x2), max(x1,x2)+1):
		y = int(round(m * x + b))
		if y in range(5): points += [[x, y]]
	for y in range(min(y1,y2), max(y1,y2)+1):
		x = int(round((y - b)/m))
		if x in range(5): points += [[x, y]]
	return points

def show(points):
	array = [[0 for i in range(5)] for i in range(5)]
	for point in points:
		array[point[0]][point[1]] = 9
	string = ':'.join(''.join(str(cell) for cell in row) for row in array)
	image = Image(string)
	display.show(image)

while True:
	show(line(0, 0, 2, 1))
	sleep(1000)
	show(line(0, 0, 1, 2))
	sleep(1000)
	show(line(4, 4, 0, 0))
	sleep(1000)
	show(line(0, 0, 1, 4))
	sleep(1000)
	#display.show(current)
	# exit(0)

