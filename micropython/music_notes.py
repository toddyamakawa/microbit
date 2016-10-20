#!/usr/bin/python
from microbit import *
import music

letters = {}
letters['A'] = "09000:90900:99900:90900:90900"
letters['B'] = "99000:90900:99000:90900:99000"
letters['C'] = "09900:90000:90000:90000:09900"
letters['D'] = "99000:90900:90900:90900:99000"
letters['E'] = "99900:90000:99000:90000:99900"
letters['F'] = "99900:90000:99000:90000:90000"
letters['G'] = "99900:90000:90000:90900:99900"

octave = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

tilt_xp = []
tilt_xp += [[ 300, 'C']]
tilt_xp += [[ 500, 'D']]
tilt_xp += [[ 600, 'E']]
tilt_xp += [[ 700, 'F']]
tilt_xp += [[ 900, 'G']]
tilt_xp += [[ 950, 'A']]
tilt_xp += [[1000, 'B']]

start_time = running_time()
while True:
	x = accelerometer.get_x()
	y = accelerometer.get_y()

	for t in tilt_xp:
		if x < t[0]:
			note = t[1]
			break

	string = letters[note]
	display.show(Image(string))

	if(button_a.get_presses() != 0):
		music.play([note + '4:4'])

