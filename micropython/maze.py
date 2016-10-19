#!/usr/bin/python
from microbit import *
import music
from random import *

def four_walls(row, col):
	if row < 1 or col < 1 or row >= 2*maze_rows or col >= 2*maze_cols:
		return 0
	return maze[row-1][col] and maze[row][col-1] and maze[row+1][col] and maze[row][col+1]

def print_maze(maze):
	for row in maze:
		for col in row:
			sys.stdout.write('#' if col else ' ')
		sys.stdout.write("\r\n")
	sys.stdout.flush

# --- Return Maze Pixel ---
def pixel(row, col):
	if row < 0 or col < 0 or row > 2*maze_rows or col > 2*maze_cols:
		return 0
	return maze[row][col]

# --- Get Tilt ---
def get_tilt():
	tolerance = 20
	x = accelerometer.get_x()
	y = accelerometer.get_y()
	if abs(x) > abs(y):
		if x > tolerance:
			return [0, 1]
		elif x < -tolerance:
			return [0, -1]
		else:
			return [0, 0]
	else:
		if y > tolerance:
			return [1, 0]
		elif y < -tolerance:
			return [-1, 0]
		else:
			return [0, 0]

# --- Display Maze ---
def display_maze(row, col):
	array = []
	for i in range(row-2, row+3):
		# array += [[pixel(i,j) for j in range(col-2, col+3)]]
		r = []
		for j in range(col-2, col+3):
			p = 6 * pixel(i, j)
			if i == my_row and j == my_col:
				p = 2
			r += [p]
		array += [r]
	string = ':'.join(''.join(str(cell) for cell in row) for row in array)
	image = Image(string)
	display.show(image)

# --- Generate Grid ---
maze_rows = 6
maze_cols = 6
maze = [[1 for i in range(2*maze_rows+1)] for i in range(2*maze_cols+1)]
for row in range(1, 2*maze_rows, 2):
	for col in range(1, 2*maze_cols, 2):
		maze[row][col] = 0

# --- Generate Maze ---
stack = [[2*randint(0,maze_rows-1)+1, 2*randint(0,maze_cols-1)+1]]

while(stack):
	row = stack[0][0]
	col = stack[0][1]

	dirs = []
	if four_walls(row-2, col  ): dirs += [[-1, 0]]
	if four_walls(row+2, col  ): dirs += [[+1, 0]]
	if four_walls(row  , col-2): dirs += [[ 0,-1]]
	if four_walls(row  , col+2): dirs += [[ 0,+1]]

	if(dirs):
		go = dirs[randint(0, len(dirs)-1)]
		maze[row+go[0]][col+go[1]] = 0
		stack.insert(0, [row+2*go[0], col+2*go[1]])
	else:
		del stack[0]

my_row = 1
my_col = 1
display_row = 1
display_col = 1
fail_tune = ['C4:2']
while True:
	display_maze(display_row, display_col)
	move = get_tilt()
	if(button_a.get_presses() > 0):
		if [my_row, my_col] == [display_row, display_col]:
			if maze[my_row+move[0]][my_col+move[1]]:
				music.play(fail_tune)
			else:
				my_row += move[0]
				my_col += move[1]
		display_row = my_row
		display_col = my_col
	if(button_b.get_presses() > 0):
		display_row += move[0]
		display_col += move[1]
	sleep(10)

