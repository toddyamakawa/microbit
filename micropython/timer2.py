from microbit import *
from random import *

path = []
path += [[0,0]]
path += [[0,1]]
path += [[0,2]]
path += [[0,3]]
path += [[0,4]]
path += [[1,4]]
path += [[2,4]]
path += [[3,4]]
path += [[4,4]]
path += [[4,3]]
path += [[4,2]]
path += [[4,1]]
path += [[4,0]]
path += [[3,0]]
path += [[2,0]]
path += [[1,0]]

def show(pixels):
	grid = [[0 for i in range(5)] for i in range(5)]
	for pixel in pixels:
		grid[pixel[0]][pixel[1]] = 9
	string = ':'.join(''.join(str(cell) for cell in row) for row in grid)
	image = Image(string)
	display.show(image)

start_time = running_time()

while True:
	if(button_a.get_presses() != 0): start_time = running_time()
	ms = running_time() - start_time
	start = int((ms % 1000)/(1000.0/16))
	sec = int(round(ms/1000))
	size = sec + 1
	show((path[start:]+path[:start])[0:size])
	sleep(10)

