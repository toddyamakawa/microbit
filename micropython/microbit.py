import time
from datetime import datetime

def sleep(ms):
	time.sleep(ms/1000)

def Image(string):
	return string

class Display:
	def show(self, image):
		print(image)

display = Display()


microbit_start_time = datetime.now()
def running_time():
	return (datetime.now() - microbit_start_time).microseconds

