#!/usr/bin/python
from microbit import *
from random import *

digit = []
digit += ["09990:09090:09090:09090:09990"]
digit += ["00900:09900:00900:00900:09990"]
digit += ["09990:00090:09990:09000:09990"]
digit += ["09990:00090:09990:00090:09990"]
digit += ["09090:09090:09990:00090:00090"]
digit += ["09990:09000:09990:00090:09990"]
digit += ["09990:09000:09990:09090:09990"]
digit += ["09990:00090:00090:00900:00900"]
digit += ["09990:09090:09990:09090:09990"]
digit += ["09990:09090:09990:00090:09990"]

def stack(value):
	if value == 0: return 0
	return 1 + stack(value - 1)

value = 1
while True:
	value = stack(value)
	string = digit[value % 10]
	display.show(Image(string))
	sleep(1000)
	value += 1


