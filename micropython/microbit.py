import time
from datetime import datetime

def sleep(ms):
	time.sleep(ms/1000.0)

def Image(string):
	return string

class Display:
	def show(self, image):
		print("\033c")
		print('+'+'-'*11+'+')
		for row in image.split(':'):
			row = ' '.join(list(row.replace('0', ' ')))
			print('| ' + row + ' |')
		print('+'+'-'*11+'+')
		sleep(100)

display = Display()


microbit_start_time = datetime.now()
def running_time():
	return (datetime.now() - microbit_start_time).microseconds

