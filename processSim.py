from multiprocessing import Process,set_start_method
from cmd import Cmd

class t(Cmd):
	intro='                                         _______ __\n.-----.----.-----.----.-----.-----.-----|     __|__|--------.\n|  _  |   _|  _  |  __|  -__|__ --|__ --|__     |  |        |\n|   __|__| |_____|____|_____|_____|_____|_______|__|__|__|__|\n|__|						by panic\n'
	prompt='pSim>'
	importlist=['Process from multiprocessing','Cmd from cmd'] #initialize list of imports with default imported modules
	pdict={} #dictionary of user-defined processes

	def do_import(self,arg): #command to import modules import arg[0] from arg[2]
		arg=str.split(arg)
		if len(arg)==1:
			try:
				globals()[arg[0]]=__import__(arg[0])
				t.importlist.append(arg[0])
			except:
				print('Error: module ',arg[0],' does not exist')
		elif len(arg)==3 and arg[1]=='as':
			try:
				globals()[arg[2]]=__import__(arg[0])
				t.importlist.append(' '.join(arg))
			except:
				print('Error: module ',arg[0],' does not exist')
		else:
			print('Error: invalid syntax')
		
	def do_importlist(self,arg): #displays list of imported modules
		for i in t.importlist:
			print(i)

	def do_plist(self,arg): #displays list of user-defined processes
		for i in t.pdict:
			print(i)
			
	def do_create(self,arg): #command to define a process as an imported function--no support for arguments
		arg=str.split(arg)
		if len(arg)==1:
			t.pdict[arg[0]]=Process(target=eval(arg[0]))
		elif len(arg)==3 and arg[1]=='as':
			t.pdict[arg[2]]=Process(target=eval(arg[0]))
		else:
			print('Error: invalid syntax')
	
	def do_spawn(self,arg): #spawns a new user-defined process
		if arg in t.pdict:
			try:
				t.pdict[arg].start()
			except:
				print('Error: process ',arg,' already spawned')
		else:
			print('Error: process ',arg,'not created')
	
	def do_exec(self,arg): #executes python code during runtime
		try:
			exec(arg)
		except:
			print('Error:')
	
	def do_exit(self,arg): #quits pSim
		exit()

if __name__=='__main__':
	set_start_method('spawn',force=True)
	t().cmdloop()
