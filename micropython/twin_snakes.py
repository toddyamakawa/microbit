from microbit import *
from random import *

def new_food(snake):
	while True:
		food = [randint(0,4), randint(0,4)]
		if not food in snake: return food

def choose(snake):
	head_row = snake[0][0]
	head_col = snake[0][1]
	directions = []
	if not new_head(snake,[ 0,-1]) in snake: directions+=[[ 0,-1]]
	if not new_head(snake,[ 0, 1]) in snake: directions+=[[ 0, 1]]
	if not new_head(snake,[-1, 0]) in snake: directions+=[[-1, 0]]
	if not new_head(snake,[ 1, 0]) in snake: directions+=[[ 1, 0]]
	if directions: return choice(directions)
	return []

def new_head(snake, direction):
	head_row = snake[0][0] + direction[0]
	head_col = snake[0][1] + direction[1]
	if head_row > 4: head_row = 4
	if head_row < 0: head_row = 0
	if head_col > 4: head_col = 4
	if head_col < 0: head_col = 0
	return [head_row, head_col]

def move(snake, direction):
	return [new_head(snake, direction)] + snake[0:-1]

def show(snake1, snake2, food):
	array = [[0 for i in range(5)] for i in range(5)]
	for part in snake1:
		array[part[0]][part[1]] += 4
	for part in snake2:
		array[part[0]][part[1]] += 4
	array[food[0]][food[1]] = 9
	string = ':'.join(''.join(str(cell) for cell in row) for row in array)
	image = Image(string)
	display.show(image)

start_length = 2
snake1 = [[0,0] for i in range(start_length)]
snake2 = [[4,4] for i in range(start_length)]
food = [2,2]

while True:
	show(snake1, snake2, food)
	dir1 = choose(snake1 + snake2)
	dir2 = choose(snake2 + snake1)
	if not dir1:
		snake1 = [[0,0] for i in range(start_length)]
		dir1 = choose(snake1)
	if not dir2:
		snake2 = [[0,0] for i in range(start_length)]
		dir2 = choose(snake2)
	tail1 = snake1[-1]
	tail2 = snake2[-1]
	snake1 = move(snake1, dir1)
	snake2 = move(snake2, dir2)
	if snake1[0] == food:
		food = new_food(snake1 + snake2)
		snake1 += [tail1]
	if snake2[0] == food:
		food = new_food(snake2)
		snake2 += [tail2]
	sleep(100)

