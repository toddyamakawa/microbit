#!/usr/bin/python
from microbit import *

def show_tilt(x, y):
	tolerance = 20
	if abs(x) > abs(y):
		if x > tolerance:
			display.show(Image.ARROW_E)
		elif x < -tolerance:
			display.show(Image.ARROW_W)
		else:
			display.show(Image.DIAMOND)
	else:
		if y > tolerance:
			display.show(Image.ARROW_S)
		elif y < -tolerance:
			display.show(Image.ARROW_N)
		else:
			display.show(Image.DIAMOND)

while True:

	x = accelerometer.get_x()
	y = accelerometer.get_y()
	show_tilt(x, y)

