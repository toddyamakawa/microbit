#!/usr/bin/python
from microbit import *
from random import *

def four_walls(row, col):
	if row < 1 or col < 1 or row > 2*maze_rows or col > 2*maze_cols:
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

# --- Display Maze ---
def display_maze(row, col):
	array = []
	for i in range(row-2, row+3):
		array += [[pixel(i,j) for j in range(col-2, col+3)]]
		# r = []
		# for j in range(col-2, col+3):
			# r += [pixel(i, j)]
		# array += [r]
	array[2][2] = 9
	string = ':'.join(''.join(str(cell) for cell in row) for row in array)
	image = Image(string)
	display.show(image)

# --- Generate Grid ---
maze = []
maze_rows = 10
maze_cols = 10

for row in range(0, 2*maze_rows+1):
	walls = [1 for i in range(0, 2*maze_cols+1)]
	if(row % 2):
		walls[1::2] = [0 for i in range(0, maze_cols)]
	maze += [walls]


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

# print_maze(maze)
display_maze(1,5)
# display_maze(1,1)
# display_maze(19,19)
# while True:

