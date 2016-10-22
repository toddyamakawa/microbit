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

notes = {}
notes['C4' ] = 262
notes['C#4'] = 277
notes['Db4'] = 277
notes['D4' ] = 294
notes['D#4'] = 311
notes['Eb4'] = 311
notes['E4' ] = 330
notes['F4' ] = 349
notes['F#4'] = 370
notes['Gb4'] = 370
notes['G4' ] = 392
notes['G#4'] = 415
notes['Ab4'] = 415
notes['A4' ] = 440
notes['A#4'] = 466
notes['Bb4'] = 466
notes['B4' ] = 494
notes['C5' ] = 523
notes['C#5'] = 554
notes['Db5'] = 554
notes['D5' ] = 587
notes['D#5'] = 622
notes['Eb5'] = 622
notes['E5' ] = 659
notes['F5' ] = 698
notes['F#5'] = 740
notes['Gb5'] = 740
notes['G5' ] = 784
notes['G#5'] = 831
notes['Ab5'] = 831
notes['A5' ] = 880
notes['A#5'] = 932
notes['Bb5'] = 932
notes['B5' ] = 988

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
tilt_x += [[1024, 'B']]

song = []

start_time = running_time()
while True:
	x = accelerometer.get_x()
	y = accelerometer.get_y()

	for t in tilt_x:
		if x < t[0]:
			note = t[1]
			break

	if y < -200 and note in sharp: note += '#'
	elif y > 200 and note in flat: note += 'b'

	display.show(Image(letters[note]))


	if(button_a.get_presses() != 0):
		song += [[note, '4']]
		music.pitch(notes[note + '4'], 500)
	elif(button_b.get_presses() != 0):
		song += [[note, '5']]
		music.pitch(notes[note + '5'], 500)
	elif accelerometer.was_gesture('face down'):
		for note in song:
			music.pitch(notes[note[0] + note[1]], 500)
			display.show(Image(letters[note[0]]))
	elif accelerometer.was_gesture('shake'):
		del song[-1]

