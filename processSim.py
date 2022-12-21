from multiprocessing import Process,set_start_method
from cmd import Cmd

class t(Cmd):
	intro='                                         _______ __\n.-----.----.-----.----.-----.-----.-----|     __|__|--------.\n|  _  |   _|  _  |  __|  -__|__ --|__ --|__     |  |        |\n|   __|__| |_____|____|_____|_____|_____|_______|__|__|__|__|\n|__|						by panic\n'
	prompt='pSim>'
	importlist=[] #list of user-imported modules
	pdict={} #dictionary of user-defined processes

	def do_import(self,arg): #command to import modules import arg[0] from arg[2]
		arg=str.split(arg)
		try:
			if len(arg)==1:
				globals()[arg[0]]=__import__(arg[0])
				t.importlist.append(arg[0])
			elif len(arg)==3 and arg[1]=='as':
				globals()[arg[2]]=__import__(arg[0])
				t.importlist.append(' '.join(arg))
			else:
				print('Error: invalid syntax')
		except:
			print('Error: module ',arg[0],' does not exist')
		
	def do_importlist(self,arg): #displays list of imported modules
		for i in t.importlist:
			print(i)

	def do_plist(self,arg): #displays list of user-defined processes
		for i in t.pdict:
			print(i)
			
	def do_create(self,arg): #command to define a process as an imported function--no support for arguments
		arg=str.split(arg)
		try:
			if len(arg)==1:
				t.pdict[arg[0]]=Process(target=eval(arg[0]))
			elif len(arg)==3 and arg[1]=='as':
				t.pdict[arg[2]]=Process(target=eval(arg[0]))
			else:
				print('Error: invalid syntax')
		except:
			print('Error: function ',arg[0],' does not exist')
	
	def do_start(self,arg): #starts a new user-defined process
		if arg in t.pdict:
			try:
				t.pdict[arg].start()
			except:
				print('Error: process',arg,' already started')
		else:
			print('Error: process ',arg,' not created')
			
	def do_kill(self,arg): #kills a process
		if arg in t.pdict:
			try:
				t.pdict[arg].terminate()
			except:
				print('Error: process ',arg,' is not alive')
		else:
			print('Error: process ',arg,' not created')
	
	def do_close(self,arg):
		if arg in t.pdict:
			try:
				t.pdict[arg].close()
			except:
				print('Error: process ',arg,' is running')
		else:
			print('Error: process ',arg,' not created')

	def do_status(self,arg): #displays process' alive status and PID
		if arg in t.pdict:
			print('Alive: ',t.pdict[arg].is_alive(),'\nPID: ',t.pdict[arg].pid)
	
	def do_exec(self,arg): #executes python code during runtime for debug purposes
		try:
			exec(arg)
		except:
			print('Error: Exec failed')
	
	def do_exit(self,arg): #quits pSim
		exit()

if __name__=='__main__':
	set_start_method('spawn')
	t().cmdloop()