# 0x12. JavaScript - Warm up

## Background Context

JavaScript is used for many things. Here, you will use JavaScript for 2 reasons:

- Scripting (same as we did with Python)
- Web front-end

## Resources

### Read or watch:

- [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity)
- [Variables](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Variables)
- [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)
- [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
- [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
- [Functions](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Functions)
- [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Object_basics)
- [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Advanced_JavaScript_objects)
- [Module patterns](https://darrenderidder.github.io/talks/ModulePatterns/#/5)
- [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
- [JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

Why JavaScript programming is amazing  
How to run a JavaScript script  
How to create variables and constants  
What are differences between var, const and let  
What are all the data types available in JavaScript  
How to use the if, if ... else statements  
How to use comments  
How to affect values to variables  
How to use while and for loops  
How to use break and continue statements  
What is a function and how do you use functions  
What does a function that does not use any return statement return  
Scope of variables  
What are the arithmetic operators and how to use them  
How to manipulate dictionary  
How to import a file

## Install Node 14

```console
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

## Install semi-standard

[Documentation](https://github.com/standard/semistandard)

```console
$ sudo npm install semistandard --global
```

## Notes

### Variables

are containers that store values. You start by declaring a variable with the let keyword,
followed by the name you give to the variable:

```javascript
let myVar;
```

is how you would declare a var in js

**Everything in JavaScript is an object and can be stored in a variable.**
e.g

```javascript
let myVar = document.querySelector("h1");
```

conditionals:

```javascript
let iceCream = "chocolate";
if (iceCream === "chocolate") {
  alert("Yay, I love chocolate ice cream!");
} else {
  alert("Awwww, but chocolate is my favorite…");
}
```

notice the opening and closing curly brackets but the construct is the same as in C
or python
semicolon similarity with c PL
