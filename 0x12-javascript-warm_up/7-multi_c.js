#!/usr/bin/node
const x = parseInt(process.argv[2]);
/* parseInt() returnsAn integer parsed from the given string,
or NaN when:
the radix as as a 32-bit integer is smaller than 2 or bigger than 36, or
the first non-whitespace character cannot be converted to a number.
*/
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
