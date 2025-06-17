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

=== means strictly equal, This performs a test to see if two values are equal and
of the same data type.  
notice the opening and closing curly brackets but the construct is the same as in C
or python  
semicolon similarity with c PL

## Functions

You can also define your own functions. In the next example, we create a simple function
which takes two numbers as arguments and multiplies them:

```javascript
function multiply(num1, num2) {
  let result = num1 * num2;
  return result;
}
```

### Event handlers

re code structures that listen for activity in the browser, and run code in response. The most obvious example is handling the _click_ event, which is fired by the browser when you click on something with your mouse.

```javascript
document.querySelector("html").addEventListener("click", function () {
  alert("Ouch! Stop poking me!");
});
```

There are a number of ways to attach an event handler to an element. Here we select the <html> element. We then call its addEventListener() function, passing in the name of the event to listen for ('click') and a function to run when the event happens.

The function we just passed to addEventListener() here is called an anonymous function, because it doesn't have a name. There's an alternative way of writing anonymous functions, which we call an arrow function. An arrow function uses () => instead of function ():

```javascript
document.querySelector("html").addEventListener("click", () => {
  alert("Ouch! Stop poking me!");
});
```

## Data Types

### null and undefined

Conceptually, undefined indicates the absence of a value, while null indicates the absence of an object
(which could also make up an excuse for typeof null === "object"). The language usually defaults to
undefined when something is devoid of a value:

- A return statement with no value (return;) implicitly returns undefined.
- Accessing a nonexistent object property (obj.iDontExist) returns undefined.
- A variable declaration without initialization (let x;) implicitly initializes the variable to undefined.
- Many methods, such as Array.prototype.find() and Map.prototype.get(), return undefined when no element
  is found.

## An Expression

an expression is a valid unit of code that resolves to a value. There are two types of expressions: those
that have side effects (such as assigning values) and those that purely evaluate.

## Control flow and error handling

Falsy values  
The following values evaluate to false (also known as Falsy values):

- false
- undefined
- null
- 0
- NaN
- the empty string ("")
  All other values—including all objects—evaluate to true when passed to a conditional statement.

The parseInt() function parses a string argument and returns an integer of the specified radix
(the base in mathematical numeral systems).

const originals = [1, 2, 3];

const doubled = originals.map(item => item \* 2);

console.log(doubled); // [2, 4, 6]

## Arrow functions

An anonymous function has no name. You'll often see anonymous functions when a function expects to receive another function as a parameter. In this case, the function parameter is often passed as an anonymous function.

If you pass an anonymous function like this, there's an alternative form you can use, called an arrow function. Instead of function(event), you write (event) =>:

```javascript
textBox.addEventListener("keydown", (event) => {
  console.log(`You pressed "${event.key}".`);
});
```

If the function only takes one parameter, you can omit the parentheses around the parameter:

```javascript
textBox.addEventListener("keydown", (event) => {
  console.log(`You pressed "${event.key}".`);
});
```

Finally, if your function contains only one line that's a return statement, you can also omit the braces and the return keyword and implicitly return the expression. In the following example, we're using the _map()_ method of ` Array` to double every value in the original array:

```javascript
const originals = [1, 2, 3];
const doubled = originals.map((item) => item * 2);
console.log(doubled); // [2, 4, 6]
```

The map() method takes each item in the array in turn, passing it into the given function. It then takes the value returned by that function and adds it to a new array.
