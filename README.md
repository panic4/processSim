# processSim
processSim is a Python command-line interface for spawning and controlling Python functions as processes.
## Commands
### ```import```
Imports modules. Also works with local modules in the same folder as processSim.py
```
pSim>import example
```
Modules can also be imported with an alias using the ```as``` keyword.
```
pSim>import example as e
```
### ```create```
Defines a process as a user-imported function. Arguments are passed after the function name.
```
pSim>create e.idle 10
```
Processes can also be created with a custom name using the ```as``` keyword.
```
pSim>create e.idle 10 as idle
```
### ```start```
Starts a process made with the ```create``` command.
```
pSim>start idle
```
### ```kill```
Kills a running process.
```
pSim>kill idle
```
### ```close```
Closes a process, releasing its resources. Processes must be killed before they can be closed.
```
pSim>close idle
```
### ```status```
Prints whether a process is alive and its PID.
```
psim>status idle
Alive: False
PID: 4267
```
### ```importlist```
Prints all user-imported modules.
```
pSim>importlist
example as e
```
### ```processlist```
Prints all user-defined processes.
```
pSim>processlist
idle
```
### ```help```
Prints a help message.
```
pSim>help

Documented commands (type help <topic>):
close   exit  import      kill         shell  status
create  help  importlist  processlist  start
```
For detailed help with a specific command, pass the command as an argument.
```
pSim>help import
Imports modules.
Usage: import [module]; import [module] as [alias]
```
The ```help``` command can also be used with the ```?``` keyword:
```
pSim>?import
Imports modules.
Usage: import [module]; import [module] as [alias]
```
### ```shell```
Executes Python code during runtime. For debugging purposes; please don't open an issue involving this command. I will cry.
```
pSim>shell print('foobar')
foobar
```
The ```shell``` command can also be used with the ```!``` keyword:
```
pSim>!print('foobar')
foobar
```
## License
This software is dedicated to the public domain with the [Unlicense](https://unlicense.org).