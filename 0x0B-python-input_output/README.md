# 0x0B. Python - Input/Output
## Notes
    f = open('workfile', 'w', encoding="utf-8")
open() returns a file object, and is most commonly used with two positional arguments and one keyword   argument: *open(filename, mode, encoding=None)*  
The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.  
+ Because UTF-8 is the modern de-facto standard, encoding="utf-8" is recommended unless you know that you need to use a different encoding. 
+ Appending a 'b' to the mode opens the file in binary mode. Binary mode data is read and written as bytes objects. You can not specify encoding when opening file in binary mode.
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
    
If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

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
 Numbers take a bit more effort, since the read() method only returns strings, which will have to be passed to a function like int(), which takes a string like '123' and returns its numeric value 123  
 Rather than having users constantly writing and debugging code to save complicated data types to files, Python allows you to use the popular data interchange format called JSON (JavaScript Object Notation). The standard module called json can take Python data hierarchies, and convert them to string representations; this process is called serializing. Reconstructing the data from the string representation is called deserializing. Between serializing and deserializing, the string representing the object may have been stored in a file or data, or sent over a network connection to some distant machine.  
 f you have an object x, you can view its JSON string representation with a simple line of code:

    import json
    x = [1, 'simple', 'list']
    json.dumps(x)
    '[1, "simple", "list"]'

Another variant of the dumps() function, called dump(), simply serializes the object to a text file. So if f is a text file object opened for writing, we can do this:

    json.dump(x, f)

To decode the object again, if f is a binary file or text file object which has been opened for reading:

    x = json.load(f)

**Note:** JSON files must be encoded in UTF-8. Use encoding="utf-8" when opening JSON file as a text file for both of reading and writing.

## Links
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files  