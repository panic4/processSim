#file containing an example function to import into processSim
from time import sleep

def idle(arg):
	try:
		sleep(arg)
	except:
		print('example.idle error: invalid argument')