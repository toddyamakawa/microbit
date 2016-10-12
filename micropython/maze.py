#!/usr/bin/python
# from microbit import *
from random import *

maze = []
maze_rows = 10
maze_cols = 10

for row in range(0, 2*maze_rows+1):
	walls = [1 for i in range(0, 2*maze_cols+1)]
	if(row % 2):
		walls[1::2] = [0 for i in range(0, maze_cols)]
	maze += [walls]

def print_maze(maze):
	for row in maze:
		for col in row:
			print('#' if col else ' ', end='')
		print("")

stack = [[2*randint(0,maze_rows-1)+1, 2*randint(0,maze_cols-1)+1]]

def four_walls(row, col):
	if row < 1 or col < 1 or row > 2*maze_rows or col > 2*maze_cols:
		return 0

	walls = 0
	if maze[row-1][col  ]: walls += 1
	if maze[row  ][col-1]: walls += 1
	if maze[row+1][col  ]: walls += 1
	if maze[row  ][col+1]: walls += 1
	return walls == 4

while(stack):
	dirs = []
	row = stack[0][0]
	col = stack[0][1]

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


print_maze(maze)


