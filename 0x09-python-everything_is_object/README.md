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


## Links 

Objects
http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values 