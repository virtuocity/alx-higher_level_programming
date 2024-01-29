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

## Links
+ [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” (excluded))
+ [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The __init__ Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “__str__- and __repr__-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
+ [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php )
classmethods and staticmethods
+ [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php) (Mainly the last part “Public instead of Private Attributes”)
+ [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)
+ [Class vs. Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)    
+ [Object Oriented Programming](https://python.swaroopch.com/oop.html )  
