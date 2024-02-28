# 0x08. Python - More Classes and Objects
## Notes
*Encapsulation* is seen as the bundling of data with the methods that operate on them. These methods are of course the getter for retrieving the data and the setter for changing the data. According to this principle, the attributes of a class are made private to hide and protect them.   
Be careful, if you want to change a class attribute, you have to do it with the notation ClassName.AttributeName. Otherwise, you will create a new instance variable.  
```python
class C: 
    counter = 0
    def __init__(self): 
        type(self).counter += 1
    def __del__(self):
        type(self).counter -= 1
if __name__ == "__main__":
    x = C()
    print("Number of instances: : " + str(C.counter))
    y = C()
    print("Number of instances: : " + str(C.counter))
    del x
    print("Number of instances: : " + str(C.counter))
    del y
    print("Number of instances: : " + str(C.counter))
```
Principially, we could have written C.counter instead of *type(self).counter*, because type(self) will be evaluated to "C" anyway. However we will understand later, that type(self) makes sense, if we use such a class as a superclass.  

str()	
+ make object readable	
+ generate output for end user	

repr()
+ need code that reproduces object  
+ generate output for developer
### Static Methods
A method that can be called without a reference to the instace i.e *self*. AAlso a method  can be called via the class name or via the instance name without the necessity of passing a reference of an instance to it. One adds the decorator *@staticmethod* before the method definition. 

```python
class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    @staticmethod
    def RobotInstances():
        return Robot.__counter
if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())
```
OUTPUT:
0
1
2
2
### Class Methods
Like static methods class methods are not bound to instances, but unlike static methods class methods are bound to a class. The first parameter of a class method is a reference to a class, i.e. a class object. They can be called via an instance or the class name.

```python
class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter
if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())
```

Use cases:
+ They are often used, where we have static methods, which have to call other static methods. To do this, we would have to hard code the class name, if we had to use static methods. This is a problem, if we are in a use case, where we have inherited classes.  

## Links
+ [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” (excluded))
+ [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The __init__ Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “__str__- and __repr__-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
+ [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php )
classmethods and staticmethods
+ [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php) (Mainly the last part “Public instead of Private Attributes”)
+ [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)   
+ [Object Oriented Programming](https://python.swaroopch.com/oop.html )  
