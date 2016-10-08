#!/usr/bin/python
from microbit import *

def show_gesture(gesture):
	if gesture == 'up':
		display.show(Image.ARROW_S)
	elif gesture == 'down':
		display.show(Image.ARROW_N)
	elif gesture == 'left':
		display.show(Image.ARROW_W)
	elif gesture == 'right':
		display.show(Image.ARROW_E)
	else:
		display.show(Image.DIAMOND)

def button_pressed():
	sleep(10)
	a = button_a.get_presses()
	b = button_b.get_presses()
	return a + b != 0

while True:

	display.show(Image.HAPPY)
	sleep(1000)

	while not button_pressed():
		answer = accelerometer.current_gesture()
		show_gesture(answer)

	display.show(Image.SURPRISED)
	sleep(1000)

	guess = 'none'
	while guess != answer:
		while not button_pressed():
			guess = accelerometer.current_gesture()
			show_gesture(guess)
		if guess != answer:
			display.show(Image.SAD)
			sleep(1000)

