# 0x07. Python - Test-driven development
## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
+ Why Python programming is awesome
+ What’s an interactive test
+ Why tests are important
+ How to write Docstrings to create tests
Through doctests
+ How to write documentation for each module and function

+ What are the basic option flags to create tests
+ How to find edge cases
## Notes and Thoughts
Testing is the process of evaluating a system or its component(s) with the intent to find whether it satisfies the specified requirements or not.

**Code that is not tested can’t be trusted**

### Functional Testing
This is a type of black-box testing that is based on the specifications of the software that is to be tested. The application is tested by providing input and then the results are examined that need to conform to the functionality it was intended for. 
### Unit Testing
Unit testing is performed by the respective developers on the individual units of source code assigned areas. The goal of unit testing is to isolate each part of the program and show that individual parts are correct in terms of requirements and functionality. 
Integration Testing
Integration testing is defined as the testing of combined parts of an application to determine if they function correctly. Integration testing can be done in two ways: Bottom-up integration testing and Top-down 

### Integration testing.
Integration testing is defined as the testing of combined parts of an application to determine if they function correctly. Integration testing can be done in two ways: Bottom-up integration testing and Top-down integration testing.

+ Bottom-up integration: This testing begins with unit testing, followed by tests of progressively higher-level combinations of units called modules or builds.
+ Top-down integration: In this testing, the highest-level modules are tested first and progressively, lower-level modules are tested thereafter.

### System Testing

System testing tests the system as a whole. Once all the components are integrated, the application as a whole is tested rigorously to see that it meets the specified Quality Standards. 

Think of how you might test the lights on a car. You would turn on the lights (known as the test step) and go outside the car or ask a friend to check that the lights are on (known as the test assertion). Testing multiple components is known as *integration testing*. 

### Python If with NOT Operator

    if not value:
        statement(s)

If value is of boolean type, then NOT acts a negation operator. If value is False, not value would be True, and the statement(s) in if-block will execute. If value is True, not value would be False, and the statement(s) in if-block will not execute.

If value is of type string, then statement(s) in if-block will execute if string is empty.

If value is of type list, then statement(s) in if-block will execute if list is empty. The same explanation holds correct for value of other collection datatypes: dict, set and tuple.

### What is Doctest?
Doctest is an inbuilt test framework that comes bundled with Python by default. The doctest module searches for code fragments that resemble interactive Python sessions and runs those sessions to confirm they operate as shown

Developers commonly use doctest to test documentation. The doctest module looks for sequences of prompts in a docstring, re-executes the extracted command, and compares the output with the command’s input given in the docstrings test example.

The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. There are several common ways to use doctest:

+ To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.
+ To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
+ To write tutorial documentation for a package, liberally illustrated with input-output examples. Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.

Here’s a complete but small example module:

```python
    """
This is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large
    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
In the above code example, to check if a number is float, the following is used

```python
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
```

since math.floor(2.14) = 2 and 2.14 != 2!

and to check for very large numbers:

   ```python
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
   ```

for large numbers such as 1e300, python trucates the value of 1e300 + 1 to 1e300 hence if n = 1e300, n+1 == n

*doctest* also allows for surrounding text. It looks for lines beginning with the interpreter prompt (>>>) to find the beginning of a test case, and the case is ended by a blank line or by the next interpreter prompt

When the tests include values that are likely to change in unpredictable ways, and where the actual value is not important to the test results, use the ELLIPSIS option to tell doctest to ignore portions of the verification value.
### What is Unittest?
Unittest test case runners allow more options when running tests, like reporting test statistics such as tests that passed and failed.

Unittest uses methods created in classes to manage tests. It has support for automation, setup, and shutdown code when testing. Unittest has several rich, in-built features that are unavailable in doctest, including generators and group fixture managers like setUp and tearDown. 

Since unittest follows the object-oriented method, it’s more suitable for testing class-based methods in a non-production environment.

 Unit test supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

To achieve this, unittest supports some important concepts in an object-oriented way:

*test fixture*  
A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

*test case*
A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.

*test suite*
A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.

*test runner*
A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.

**Look out for all edge cases!!!!!**

## Resources
### Read or watch:
+ [Software Testing](https://alx-intranet.hbtn.io/concepts/47)
+ [doctest — Test interactive Python examples (until “26.2.3.7. Warnings” included)](https://docs.python.org/3.4/library/doctest.html)
+ [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
[Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)
+ [Unittest module](https://www.youtube.com/watch?v=6tNS--WetLI)
+ [Interactive and Non-interactive tests](https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/)
+ [Python docs unit testing  ](https://docs.python.org/3/library/unittest.html)
+ [Getting started with testing in python](https://realpython.com/python-testing/)
+ [Python If with NOT Operator](https://pythonexamples.org/python-if-not/)