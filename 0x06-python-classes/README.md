# 0x06. Python - Classes and Objects
## Notes and Thoughts
+ Classes and objects are the two main aspects of object oriented programming
+ A class creates a new type where objects are instances of the class
+ Objects can store data using ordinary variables that belong to the object. Variables that belong to an object or class are referred to as fields  
+ Objects can also have functionality by using functions that belong to a class. Such functions are called methods of the class
+ Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called instance variables and class variables respectively.
+ A class is created using the class keyword. 

### The __init__ method
The __init__ method is run as soon as an object of a class is instantiated (i.e. created). The method is useful to do any initialization (i.e. passing initial values to your object)
### Data encapsualtion, abstraction and information hiding
*Data encapsulation* is the bundling of data together with the methods that operate on that data. *Information hiding* on the other hand is the principle that some internal information or data is "hidden", so that it can't be accidentally changed. *Data abstraction*  is present, if both data hiding and data encapsulation is used.

Encapsulation is often achieved using getters and setters
### cls - class methods
```python
    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))
```
The how_many is actually a method that belongs to the class and not to the object. This means we can define it as either a classmethod or a staticmethod depending on whether we need to know which class we are part of. Since we refer to a class variable, let's use classmethod.  

We have marked the how_many method as a class method using a decorators:  
### Decorators
Decorators can be imagined to be a shortcut to calling a wrapper function (i.e. a function that "wraps" around another function so that it can do something before or after the inner function), so applying the **@classmethod* decorator is the same as calling:  
    how_many = classmethod(how_many)

### Properties vs. Getters and Setters
Getters(also known as 'accessors') and setters (aka. 'mutators') are used in many object oriented programming languages to ensure the principle of data encapsulation  
*Encapsulation* is seen as the bundling of data with the methods that operate on them. These methods are of course the getter for retrieving the data and the setter for changing the data.  

The class with a property looks like this:
```python
class P:
    def __init__(self, x):
        self.x = x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
```
A method which is used for getting a value is decorated with "@property", i.e. we put this line directly in front of the header. The method which has to function as the setter is decorated with "@x.setter". If the function had been called "f", we would have to decorate it with "@f.setter". Two things are noteworthy: We just put the code line "self.x = x" in the __init__ method and the property method x is used to check the limits of the values. The second interesting thing is that we wrote "two" methods with the same name and a different number of parameters "def x(self)" and "def x(self,x)". We have learned in a previous chapter of our course that this is not possible. It works here due to the decorating.  

### __str__ and __repr__ methods
Are magic methods "__str__" and "__repr__". 

## Links
+ [Python OOP](https://python.swaroopch.com/oop.html)
+ [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) 
+ [Decorators](https://python.swaroopch.com/more.html#decorator) 
+ [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
+ [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)