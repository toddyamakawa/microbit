#!/usr/bin/python
from microbit import *
import music

letters = {}

letters['C'] = "09900:90000:90000:90000:09900"
letters['D'] = "99000:90900:90900:90900:99000"
letters['E'] = "99900:90000:99000:90000:99900"
letters['F'] = "99900:90000:99000:90000:90000"
letters['G'] = "99900:90000:90000:90900:99900"
letters['A'] = "09000:90900:99900:90900:90900"
letters['B'] = "99000:90900:99000:90900:99000"

letters['C#'] = "09909:90000:90000:90000:09900"
letters['D#'] = "99009:90900:90900:90900:99000"
letters['F#'] = "99909:90000:99000:90000:90000"
letters['G#'] = "99909:90000:90000:90900:99900"
letters['A#'] = "09009:90900:99900:90900:90900"

letters['Db'] = "99000:90900:90900:90900:99009"
letters['Eb'] = "99900:90000:99000:90000:99909"
letters['Gb'] = "99900:90000:90000:90900:99909"
letters['Ab'] = "09000:90900:99900:90900:90909"
letters['Bb'] = "99000:90900:99000:90900:99009"

octave = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
sharp = ['C', 'D', 'F', 'G', 'A']
flat = ['D', 'E', 'G', 'A', 'B']

tilt_x = []
tilt_x += [[-700, 'C']]
tilt_x += [[-500, 'D']]
tilt_x += [[-200, 'E']]
tilt_x += [[ 200, 'F']]
tilt_x += [[ 500, 'G']]
tilt_x += [[ 700, 'A']]
tilt_x += [[1000, 'B']]

start_time = running_time()
while True:
	x = accelerometer.get_x()
	y = accelerometer.get_y()

	for t in tilt_x:
		if x < t[0]:
			note = t[1]
			break

	accidental = ''
	if y < -100 and note in sharp: accidental = '#'
	if y > 100 and note in flat: accidental = 'b'

	note = note + accidental

	string = letters[note]
	display.show(Image(string))

	if(button_a.get_presses() != 0):
		music.play([note + accidental + '4:4'])

	if(button_b.get_presses() != 0):
		music.play([note + accidental + '5:4'])


