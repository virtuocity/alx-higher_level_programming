# 0x01. Python - if/else, loops, functions

## Notes and Thoughts
Indentation is very important in python. 

Compound statements (loops...for ....while ,conditionals if....elif....else...), contain (groups of) other statements; they affect or control the execution of those other statements in some way. 

*try* specifies exception handlers and/or cleanup code for a group of statements, while the *with* statement allows the execution of initialization and finalization code around a block of code. *Function and class* definitions are also syntactically compound statements.
A compound statement consists of one or more ‘clauses.’ A clause consists of a header and a ‘suite.’ 

 A suite can be one or more semicolon-separated simple statements on the same line as the header, following the header’s colon, or it can be one or more indented statements on subsequent lines.

 

	range()  
-returns a sequence of numbers ,starting from 0 by default and increments by 1 (by default) and stops before  
a specified number.  
**range(start, stop, step)**  

*Number Randomizer*  

	import random

	number = random.randint(-10,000, 10000)

### Functions
From a function's perspective:  

A parameter is the variable listed inside the parentheses in the function definition.  

An argument is the value that is sent to the function when it is called.  

#### Arbitrary Arguments,args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in  
the function definition.  

## Tasks

## Links
PEP
https://peps.python.org/pep-0008/  
range  
https://www.w3schools.com/python/ref_func_range.asp  
Control flow tools  
https://docs.python.org/3/tutorial/controlflow.html  
Compound statements  
https://docs.python.org/3/reference/compound_stmts.html#while 
pass  
https://www.w3schools.com/python/ref_keyword_pass.asp#:~:text=The%20pass%20statement%20is%20used,definitions%2C%20or%20in%20if%20statements.  

