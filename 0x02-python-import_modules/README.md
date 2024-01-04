# 0x02. Python - import & modules
## Learning Objectives
**At the end of this project, you are expected to be able to explain to anyone, without the help of Google:**

### General
Why Python programming is awesome  
How to import functions from another file  
How to use imported functions  
How to create a module  
How to use the built-in function *dir()*  
How to prevent code in your script from being executed when imported  
How to use command line arguments with your Python programs  

## Notes and Thoughts
Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter.  

*A module* is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended.  

*definitions* from a module can be imported into other modules or into the main module (the collection of variables that you have access to in a script executed at the top level and in calculator mode).  
Within a module, the module’s name (as a string) is available as the value of the global variable __name__   

A *namespace* is the place where variables are stored. Namespaces are implemented as dictionaries.There are the local, global and built-in namespaces as well as nested namespaces in objects (in methods). Namespaces support modularity by preventing naming conflicts. For instance, the functions builtins.open and os.open() are distinguished by their namespaces. 

The imported module names, if placed at the top level of a module (outside any functions or classes), are added to the module’s global namespace.  

## Random
A good commit message will explain the why behind your changes. In other words, a commit message describes what problem your changes solve and how it solves them.  

5 Steps To Improve Your Git Messages: 

+ **Capitalization and Punctuation:** The first word should be capitalized and not end in punctuation.
+ **Commit type:** The type of the commit has to be specified to describe your changes. You could use: *Bugfix, Refactor, Hotfix*  
+ **Length:** The first line should not be longer than 50 characters and the body should be restricted to a line length of 72 - see Linus Torvalds explanation or this helpful guide  
+ **Mood:** Always use imperative mood in the subject because it gives the tone you are giving an order or request  
+ **Content:**Direct sentences without phrases like: though, I think, kind
Content is very important and if you write it you should consider and answer the following questions while you write it down:

What is the reason for these changes?  
What was the effect that my changes made?  
Why was the change needed?  
What are the changes in reference to?  
## Resources
Read or watch:

+ [Modules](https://docs.python.org/3/tutorial/modules.html)
+ [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
