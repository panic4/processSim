from multiprocessing import Process,set_start_method
import cmd

class t(cmd.Cmd):
	intro='                                         _______ __\n.-----.----.-----.----.-----.-----.-----|     __|__|--------.\n|  _  |   _|  _  |  __|  -__|__ --|__ --|__     |  |        |\n|   __|__| |_____|____|_____|_____|_____|_______|__|__|__|__|\n|__|						by panic\n'
	prompt='pSim>'
	ruler=None
	importlist=[] #list of user-imported modules
	pdict={} #dictionary of user-defined processes

	def do_import(self,arg):
		'''Imports modules.\nUsage: import [module]; import [module] as [alias]'''
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
			print('Error: module',arg[0],'does not exist or has already been imported')
		
	def do_importlist(self,arg):
		'''Displays list of user-imported modules.\nUsage: importlist'''
		for i in t.importlist:
			print(i)

	def do_processlist(self,arg):
		'''Displays list of processes defined using the create command.\nUsage: processlist'''
		for i in t.pdict:
			print(i)
			
	def do_create(self,arg):
		'''Defines a process as a user-imported method.\nUsage: create [method]; create [method] as [process name]'''
		arg=str.split(arg)
		try:
			if len(arg)==1:
				t.pdict[arg[0]]=Process(target=eval(arg[0]))
			elif len(arg)==3 and arg[1]=='as':
				t.pdict[arg[2]]=Process(target=eval(arg[0]))
			else:
				print('Error: invalid syntax')
		except:
			print('Error: function',arg[0],'does not exist')
	
	def do_start(self,arg):
		'''Starts a new user-defined process.\nUsage: start [process name]'''
		if arg in t.pdict:
			try:
				t.pdict[arg].start()
			except:
				print('Error: process',arg,'already started')
		else:
			print('Error: process',arg,'not created')
			
	def do_kill(self,arg):
		'''Kills a process.\nUsage: kill [process name]'''
		if arg in t.pdict:
			try:
				t.pdict[arg].terminate()
			except:
				print('Error: process',arg,'is not alive')
		else:
			print('Error: process',arg,'not created')
	
	def do_close(self,arg):
		'''Closes a process and releases its resources.\nUsage: close [process name]'''
		if arg in t.pdict:
			try:
				t.pdict[arg].close()
				del t.pdict[arg]
			except:
				print('Error: process',arg,'is running')
		else:
			print('Error: process',arg,'not created')

	def do_status(self,arg):
		'''Displays a process' alive status and PID.\nUsage: status [process name]'''
		if arg in t.pdict:
			try:
				print('Running:',t.pdict[arg].is_alive(),'\nPID:',t.pdict[arg].pid)
			except:
				print('Error: process is closed')
		else:
			print('Error: process',arg,'not created')
	
	def do_shell(self,arg):
		'''Executes Python code during runtime.\nUsage: shell [argument]; ![argument]'''
		exec(arg)
	
	def do_exit(self,arg):
		'''Kills all processes and quits processSim.\nUsage: exit'''
		for i in t.pdict:
			t.do_kill(self,i)
		exit()

if __name__=='__main__':
	set_start_method('spawn')
	try:
		t().cmdloop()
	except:
		t.do_exit(None,None)
