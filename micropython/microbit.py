import sys
import time
from datetime import datetime

def sleep(ms):
	time.sleep(ms/1000.0)

def Image(string):
	return string

class Display:
	def show(self, image):

		# Colors
		reset = "\033[0m"
		bright = "\033[101;91m"
		dim = "\033[41;31m"
		off = "\033[8m"
		clear = "\033c"

		# Display format
		width = 2
		empty_row = '|' + ' '*(5*(1+width)+1) + "|\n"
		header_row = '+' + '-'*(5*(1+width)+1) + "+\n"

		sys.stdout.write(clear)
		sys.stdout.write(header_row)
		for row in image.split(':'):
			sys.stdout.write('| ')
			for col in list(row):
				if(int(col) == 0):
					col = off + col + reset
				elif(int(col) >= 6):
					col = bright + col + reset
				else:
					col = dim + col + reset
				sys.stdout.write(col*width + ' ')
			sys.stdout.write("|\n")
			sys.stdout.write(empty_row)
		sys.stdout.write(header_row)
		sys.stdout.flush
		sleep(100)

display = Display()


microbit_start_time = datetime.now()
def running_time():
	return (datetime.now() - microbit_start_time).microseconds

