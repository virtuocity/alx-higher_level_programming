# 0x03. Python - Data Structures: Lists, Tuples
## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
+ Why Python programming is awesome  
+ What are lists and how to use them  
+  What are the differences and similarities between strings and lists  
+ What are the most common methods of lists and how to use them  
+ How to use lists as stacks and queues  
+ What are list comprehensions and how to use them  
+ What are tuples and how to use them  
+ When to use tuples versus lists  
+ What is a sequence  
+ What is tuple packing  
+ What is sequence unpacking  
+ What is the del statement and how to use it  

## Notes and thoughts
Lists can be written as a list of comma-separated values (items) between square brackets  
A list can contain different data types.From Python's perspective, lists are defined as objects with the data type 'list':  

	<class 'list'>

It is also possible to use the list() constructor when creating a new list.  

	thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
	print(thislist)

*A lambda function* is a small anonymous function  
It can take any number of arguments but can only have one expression  

lamda **arguements: expression**

The expression is executed and the result is returned, for example  

	x = lambda a : a + 10
	print(x(5))  

### List comprehensions
List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

```python
squares = []
for x in range(10):
	squares.append(x**2)
print(squares)
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Note that this creates (or overwrites) a variable named x that still exists after the loop completes. We can calculate the list of squares without any side effects using:

```python
squares = list(map(lambda x: x**2, range(10)))
```

or, equivalently:

```python
squares = [x**2 for x in range(10)]
```

which is more concise and readable  

A *list comprehension* consists of **brackets containing an expression followed by a for clause, then zero or more for or if clauses. The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it**. For example, this listcomp combines the elements of two lists if they are not equal:
## Resources
Read or watch:
+ [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
+ [Data structures(until 5.3. Tuples and Sequences included)](https://docs.python.org/3/tutorial/datastructures.html)
+ [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)
+  [Lambda Operator, filter, reduce and map](https://python-course.eu/advanced-python/lambda-filter-reduce-map.php)  
+ [List comprehensions](https://python-course.eu/advanced-python/list-comprehension.php )
 

	
