# 0x02. Python - import & modules
## Notes and Thoughts
Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter.  
A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.  

*definitions* from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).  
Within a module, the module’s name (as a string) is available as the value of the global variable __name__   

A *namespace* is the place where variables are stored. Namespaces are implemented as dictionaries.There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods). Namespaces support modularity by preventing naming conflicts. For instance, the functions builtins.open and os.open() are distinguished by their namespaces. 

The imported module names, if placed at the top level of a module (outside any functions or classes), are added to the module’s global namespace.  


## Links
https://docs.python.org/3/tutorial/modules.html 
