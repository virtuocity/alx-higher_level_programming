# 0x09. Python - Everything is object
## Notes and Thoughts 
An object is something a variable can refer to 

   ```python
    a = "banana"
    b = "banana
```
both a and b are objects that a variable can refer to in this case both a and b refer to the same variable.
Since strings are *immutable*, Python optimizes resources by making two names that refer to the same string value refer to the same object.
### Aliasing

```python
a = [1, 2, 3]
b = a
a is b
```
Since variables refer to objects, if we assign one variable to another, both variables refer to the same object: Because the same list has two different names, a and b, we say that it is *aliased*. Changes made with one alias affect the other:
b[0] = 5
print(a)

*cloning* - If we want to modify a list and also keep a copy of the original, we need to be able to make a copy of the list itself, not just the reference. We do this by using splicing:

```python
a = [1, 2, 3]
b = a[:]
```
```python
numbers = [1, 2, 3, 4, 5]

for index in range(len(numbers)):
    numbers[index] = numbers[index]**2
```
in  a for loop, this construct is so common that python provides a nicer way to implement it:
```python
numbers = [1, 2, 3, 4, 5]
for index,value in enumerate(numbers)
    numbers[index] = numbers[index]**2
```
*enumerate* generates both the index and the value associated with it during the list traversal.

## Links 

Objects
http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values 