#!/usr/bin/node

function factorial (n) {
  n = parseInt(n);// is it an integer or NaN?
  if (!isNaN(n)) { // do the following if int
    if (n !== 1) {
      const f = n * factorial(n - 1);
      return f;
    } else { // else it is a NaN, return 1
      return 1;
    }
  } else { // n is 1
    return 1;
  }
}
console.log(factorial(process.argv[2]));
