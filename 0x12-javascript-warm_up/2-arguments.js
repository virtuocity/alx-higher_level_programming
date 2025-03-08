#!/usr/bin/node
let numArgs;
if (process.argv.length <= 2) {
  numArgs = 'No argument';
} else if (process.argv.length === 3) {
  numArgs = 'Argument found';
} else {
  numArgs = 'Arguments found';
}
console.log(numArgs);
