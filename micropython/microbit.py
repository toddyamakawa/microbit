import time

def sleep(ms):
	time.sleep(ms/1000)

def Image(string):
	return string

class Display:
	def show(self, image):
		print(image)

display = Display()

