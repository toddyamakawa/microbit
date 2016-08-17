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

def show(snake, food):
	array = [[0 for i in range(5)] for i in range(5)]
	for part in snake:
		array[part[0]][part[1]] = 5
	array[food[0]][food[1]] = 9
	string = ':'.join(''.join(str(cell) for cell in row) for row in array)
	image = Image(string)
	display.show(image)

snake = [[0,0]]
food = new_food(snake)
count = 10

while True:
	show(snake, food)
	direction = choose(snake)
	if not direction:
		snake = [[0,0]]
		direction = choose(snake)
	tail = snake[-1]
	snake = move(snake, direction)
	if snake[0] == food:
		food = new_food(snake)
		snake += [tail]
	count -= 1
	# if count <= 0: exit(1)
	sleep(100)

