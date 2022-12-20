# 0x05. Python - Exceptions
## Notes and Thoughts
There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.  
*Syntax Errors* , also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python  
 Exceptions come in different types, and the type is printed as part of the message: the types in the example are ZeroDivisionError, NameError and  
 TypeError  
 The *finally* keyword is used in try... except blocks. It defines a block of code to run when the try... except...else block is complete  

	while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

The try statement works as follows:  
+ First, the try clause (the statement(s) between the try and except keywords) is executed  
+ If no exception occurs, the except clause is skipped and execution of the try statement is finished.  
+ If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after  
the except keyword, the except clause is executed, and then execution continues after the try/except block.  
+ If an exception occurs which does not match the exception named in the except clause, it is passed on to  
outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.  

A try statement may have more than one except clause, to specify handlers for different exceptions.  
	
	except (RuntimeError, TypeError, NameError):
		pass

The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.  
