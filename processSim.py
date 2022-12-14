from importlib import import_module
import multiprocessing as mp
import cmd
mp.set_start_method('spawn',force=True) #force processes to use spawn

importlist=['import_module from importlib','multiprocessing as mp','cmd'] #initialize list of imports with default imported modules

class t(cmd.Cmd):
	intro='                                         _______ __\n.-----.----.-----.----.-----.-----.-----|     __|__|--------.\n|  _  |   _|  _  |  __|  -__|__ --|__ --|__     |  |        |\n|   __|__| |_____|____|_____|_____|_____|_______|__|__|__|__|\n|__|						by panic\n'
	prompt='pSim>'

	#command list
	def do_import(self,arg): #command to import modules
		importlist.append(arg)
		arg=str.split(arg.lower())
		try:
			if len(arg)==1:
				globals()[arg[0]]=__import__(arg[0])
			elif len(arg)==3:
				if arg[1]=='as':
					globals()[arg[2]]=__import__(arg[0])
				else:
					raise
			else:
				raise
		except:
			print('Error: Invalid syntax.')
			importlist.pop()
	
	def do_importlist(self,arg): #displays list of imported modules
		for i in importlist:
			print(i)
	
	def do_exit(self,arg): #quits pSim
		exit()

if __name__=='__main__':
	t().cmdloop()
