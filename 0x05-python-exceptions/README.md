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

The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error  
when empty code not allowed.  
The try … except statement has an optional else clause, which, when present, must follow all except clauses. It is useful for code that must be  
executed if the try clause does not raise an exception. For example:  

	for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()	

Before an except clause’s suite is executed, details about the exception are stored in the *sys module* and can be accessed via sys.exc_info()

**Else Clause**
The optional else clause is executed if the control flow leaves the try suite, no exception was raised, and no return, continue, or break statement was executed. Exceptions in the else clause are not handled by the preceding except clauses.
**Finally clause**
If finally is present, it specifies a ‘cleanup’ handler. The try clause is executed, including any except and else clauses. If an exception occurs in any of the clauses and is not handled, the exception is temporarily saved. The finally clause is executed. If there is a saved exception it is re-raised at the end of the finally clause. If the finally clause raises another exception, the saved exception is set as the context of the new exception. If the finally clause executes a return, break or continue statement, the saved exception is discarded: