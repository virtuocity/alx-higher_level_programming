# 0x0A. Python - Inheritance
## Notes 
### Inheritance
*Inheritance* is a mechanism that allows you to create a hierarchy of classes *that share a set of properties and methods* by *deriving* a class from another class. Like this:  

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
The name BaseClassName must be defined in a scope containing the derived class definition.In place of a base class name, other arbitrary expressions are also allowed. This can be useful, for example, when the base class is defined in another module:

    class DerivedClassName(modname.BaseClassName):

Execution of a derived class definition proceeds the same as for a base class. When the class object is constructed, the base class is remembered. This is used for resolving attribute references: if a requested attribute is not found in the class, the search proceeds to look in the base class. This rule is applied recursively if the base class itself is derived from some other class.  
Python has two built-in functions that work with inheritance:

Use isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.  
 
Use issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.  
### Benefits of inheritance are: 
+ It represents real-world relationships well.
+ It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
+ It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
+ Inheritance offers a simple, understandable model structure. 
+ Less development and maintenance expenses result from an inheritance. 
### Multiple Inheritance
Python supports a form of multiple inheritance as well. A class definition with multiple base classes looks like this:  

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```
a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.  

Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls. For example:  

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```
The above example would work even if MappingSubclass were to introduce a __update identifier since it is replaced with _Mapping__update in the Mapping class and _MappingSubclass__update in the MappingSubclass class respectively.  

Python program to demonstrate error if we forget to invoke __init__() of the parent
If you forget to invoke the __init__() of the parent class then its instance variables would not be available to the child class. 

The following code produces an error for the same reason. 

```python
class A:
    def __init__(self, n='Rahul'):
        self.name = n
 
 
class B(A):
    def __init__(self, roll):
        self.roll = roll
 
 
object = B(23)
print(object.name)
```
Different types of Inheritance:
+ Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.
+ Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances.    

The *super()* builtin returns a proxy object (temporary object of the superclass) that allows us to access methods of the base class  

### Python dir
Python dir() Function
The dir() function returns all properties and methods of the specified object, without the values. This function will return all the properties and methods, even built-in properties which are default for all object

## Links
+ Inheritance  
https://docs.python.org/3/tutorial/classes.html#inheritance  
+ Multiple inheritance  
https://docs.python.org/3/tutorial/classes.html#multiple-inheritance  
+ Inheritance in Python
https://www.geeksforgeeks.org/inheritance-in-python/  
+ Learn to Program 10 : Inheritance Magic Methods  
https://www.youtube.com/watch?v=d8kCdLCi6Lk  