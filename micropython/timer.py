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

start_time = running_time()
while True:
	seconds = int(round((running_time() - start_time)/1000))
	string = digit[seconds % 10]
	display.show(Image(string))
	sleep(1000)


