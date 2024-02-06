# 0x0B. Python - Input/Output
Resources
Read or watch:

+ [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
+ [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
+ [Dive Into Python 3: Chapter 11. Files ](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf)(until “11.4 Binary Files” (included))
+ [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
+ [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU&ab_channel=DerekBanas)
+ [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) (ch. 8 p 180-183 and ch. 14 p 326-333)
+ [All about py-file I/O](https://techvidvan.com/tutorials/python-file-read-write/)
## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
Why Python programming is awesome  
How to open a file  
How to write text in a file  
How to read the full content of a file  
How to read a file line by line  
How to move the cursor in a file  
How to make sure a file is closed after using it  
What is and how to use the with statement  
What is JSON  
What is serialization  
What is deserialization  
How to convert a Python data structure to a JSON string  
How to convert a JSON string to a Python data structure  
## Notes
    f = open('workfile', 'w', encoding="utf-8")
open() returns a file object, and is most commonly used with two positional arguments and one keyword   argument: *open(filename, mode, encoding=None)*  
The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.  

+ Because UTF-8 is the modern de-facto standard, encoding="utf-8" is recommended unless you know that you need to use a different encoding. 
+ Appending a 'b' to the mode opens the file in binary mode. Binary mode data is read and written as bytes objects. **You can not specify encoding when opening file in binary mode.**
+ It is good practice to use the with keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try-finally blocks:
    ```python
    with open('workfile', encoding="utf-8") as f:
    read_data = f.read()
    We can check that the file has been properly closed
    f.close
    True
    ```
To read a file’s contents, call f.read(size), which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode). size is an optional numeric argument. When size is omitted or negative, the entire contents of the file will be read and returned.  

f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline  
For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:  

    for line in f:
        print(line, end='')
    
If you want to read all the lines of  file in a list you can also use list(f) or f.readlines().

Other types of objects need to be converted – either to a string (in text mode) or a bytes object (in binary mode) – before writing them:

```python
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)
18
```

f.write(string) writes the contents of string to the file, returning the number of characters written.  

    f.write('This is a test\n')
    15
f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.

To change the file object’s position, use f.seek(offset, whence). The position is computed from adding offset to a reference point; the reference point is selected by the whence argument. A whence value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. whence can be omitted and defaults to 0, using the beginning of the file as the reference point.

    f = open('workfile', 'rb+')
    f.write(b'0123456789abcdef')
    16
    f.seek(5)      # Go to the 6th byte in the file
    5
    f.read(1)
    b'5'
    f.seek(-3, 2)  # Go to the 3rd byte before the end
    13
    f.read(1)
    b'd'

### Saving structured data with json
 Strings can easily be written to and read from a file.  
 Numbers take a bit more effort, since the read() method only returns strings, which will have to be passed to a function like int(), which takes a string like '123' and returns its numeric value 123  
 Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows you to use the popular data interchange format called JSON (JavaScript Object Notation). The standard module called json can take Python data hierarchies, and convert them to string representations; this process is called serializing. Reconstructing the data from the string representation is called deserializing. Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.  

 If you have an object x, you can view its JSON string representation with a simple line of code:

    import json
    x = [1, 'simple', 'list']
    json.dumps(x)
    '[1, "simple", "list"]'

Another variant of the dumps() function, called dump(), simply serializes the object to a text file. So if f is a text file object opened for writing, we can do this:

    json.dump(x, f)

To decode the object again, if f is a binary file or text file object which has been opened for reading:

    x = json.load(f)

**Note:** JSON files must be encoded in UTF-8. Use encoding="utf-8" when opening JSON file as a text file for both of reading and writing.  

Encoding basic Python object hierarchies:

```python
import json
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
'["foo", {"bar": ["baz", null, 1.0, 2]}]'
print(json.dumps("\"foo\bar"))
"\"foo\bar"
print(json.dumps('\u1234'))
"\u1234"
print(json.dumps('\\'))
"\\"
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
{"a": 0, "b": 0, "c": 0}
from io import StringIO
io = StringIO()
json.dump(['streaming API'], io)
io.getvalue()
'["streaming API"]'
```

### ExceptionGroups
The builtin ExceptionGroup wraps a list of exception instances so that they can be raised together. It is an exception itself, so it can be caught like any other exception.  

   
    def f():
        excs = [OSError('error 1'), SystemError('error 2')]
        raise ExceptionGroup("There were errors:", excs)
        f()
        + Exception Group Traceback (most recent call last):
        |   File "<stdin>", line 1, in <module>
        |   File "<stdin>", line 3, in f
        | ExceptionGroup: there were problems
        +-+---------------- 1 ----------------
        | OSError: error 1
        +---------------- 2 ----------------
        | SystemError: error 2
        +------------------------------------
    try:
    f()
    except exception as e:
    print(f"caught:{type(e)}",)



