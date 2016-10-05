
import sys, tty, termios, time
from threading import Timer
from Queue import Queue

# ===========================
#    MICROPYTHON FUNCTIONS
# ===========================
# Display.show(image)
# image = Image(string)
# ms = running_time()
# sleep(ms)

class Microbit:

	# --- Timer ---
	start = time.time()
	@classmethod
	def elapsed(self):
		return int(1000*(time.time() - self.start))


buttons_queue = Queue()

class Buttons:

	buttons = dict()

	# --- Get Character ---
	fd = sys.stdin.fileno()
	attr = termios.tcgetattr(fd)
	@classmethod
	def getch(self):
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
		termios.tcsetattr(self.fd, termios.TCSADRAIN, self.attr)
		return ch

	# --- Monitor Key Presses ---
	@classmethod
	def monitor(self):
		key = ord(self.getch())
		buttons_queue.put(key)
		# print("key: " + str(key))
		if key == 3: return
		Timer(0, self.monitor).start()

	@classmethod
	def read(self):
		while not buttons_queue.empty():
			key = buttons_queue.get()
			if not key in self.buttons: self.buttons[key] = 0
			self.buttons[key] += 1
			# print(str(key) + ": " + str(self.buttons[key]))


	# --- Initialization ---
	def __init__(self, key):
		if type(key) is str: key = ord(key)
		self.key = key
		self.buttons[self.key] = 0

	def get_presses(self):
		key = self.key
		Buttons.read()
		presses = self.buttons[key]
		self.buttons[key] = 0
		return presses

button_a = Buttons('a')
button_b = Buttons('b')
Timer(0, Buttons.monitor).start()

def sleep(ms):
	time.sleep(ms/1000.0)

def Image(string):
	return string

class Display:

	# Colors
	reset = "\033[0m"
	bright = "\033[101;91m"
	dim = "\033[41;31m"
	off = "\033[8m"
	clear = "\033c"

	def show(self, image):

		# Display format
		width = 2
		empty_row = '|' + ' '*(5*(1+width)+1) + "|\r\n"
		header_row = '+' + '-'*(5*(1+width)+1) + "+\r\n"

		sys.stdout.write(self.clear)
		sys.stdout.write(header_row)
		for row in image.split(':'):
			sys.stdout.write('| ')
			for col in list(row):
				if(int(col) == 0):
					col = self.off + col + self.reset
				elif(int(col) >= 6):
					col = self.bright + col + self.reset
				else:
					col = self.dim + col + self.reset
				sys.stdout.write(col*width + ' ')
			sys.stdout.write("|\r\n")
			sys.stdout.write(empty_row)
		sys.stdout.write(header_row)
		sys.stdout.flush
		sleep(100)

display = Display()


def running_time():
	return Microbit.elapsed()

