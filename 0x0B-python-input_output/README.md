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


## Links
