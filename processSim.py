from multiprocessing import Process,set_start_method
import cmd

class t(cmd.Cmd):
	intro='                                         _______ __\n.-----.----.-----.----.-----.-----.-----|     __|__|--------.\n|  _  |   _|  _  |  __|  -__|__ --|__ --|__     |  |        |\n|   __|__| |_____|____|_____|_____|_____|_______|__|__|__|__|\n|__|				github.com/panic4/processSim\n'
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
		'''Defines a process as a user-imported function.\nUsage: create [function] [args]; create [function] [args] as [process name]'''
		arg=str.split(arg)
		try:
			if arg[len(arg)-2]=='as':
				t.pdict[arg[len(arg)-1]]=Process(target=eval(arg[0]),args=(eval(i) for i in arg if i not in (arg[0],arg[len(arg)-2],arg[len(arg)-1])))
			else:
				t.pdict[arg[0]]=Process(target=eval(arg[0]),args=(eval(i) for i in arg if i!=arg[0]))
		except:
			print('Error: function',arg[0],'is not defined')
	
	def do_start(self,arg):
		'''Starts a process.\nUsage: start [process name]'''
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
			if t.pdict[arg].is_alive():
				t.pdict[arg].terminate()
			else:
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
				print('Error: process',arg,'is alive')
		else:
			print('Error: process',arg,'not created')

	def do_status(self,arg):
		'''Displays a process' alive status and PID.\nUsage: status [process name]'''
		if arg in t.pdict:
			print('Running:',t.pdict[arg].is_alive(),'\nPID:',t.pdict[arg].pid)
		else:
			print('Error: process',arg,'not created')
	
	def do_shell(self,arg):
		'''Executes Python code during runtime.\nUsage: shell [argument]; ![argument]'''
		try:
			exec(arg)
		except:
			print('Error:')
	
	def do_exit(self,arg):
		'''Kills all running processes and quits processSim.\nUsage: exit'''
		for i in t.pdict:
			if t.pdict[i].is_alive():
				t.pdict[i].terminate()
		exit()

if __name__=='__main__':
	set_start_method('spawn')
	t().cmdloop()
