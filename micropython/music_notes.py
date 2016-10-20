#!/usr/bin/python
from microbit import *

letters = {}
letters['A'] = "09000:90900:99900:90900:90900"
letters['B'] = "99000:90900:99000:90900:99000"
letters['C'] = "09900:90000:90000:90000:09900"
letters['D'] = "99000:90900:90900:90900:99000"
letters['E'] = "99900:90000:99000:90000:99900"
letters['F'] = "99900:90000:99000:90000:90000"
letters['G'] = "99900:90000:90000:90900:99900"

octave = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

start_time = running_time()
while True:
	seconds = int(round((running_time() - start_time)/1000))
	string = letters[octave[seconds % 7]]
	display.show(Image(string))
	sleep(10)


