#!/usr/bin/node
const size = parseInt(process.argv[2]);
/* parseInt() returnsAn integer parsed from the given string,
or NaN when:
the radix as as a 32-bit integer is smaller than 2 or bigger than 36, or
the first non-whitespace character cannot be converted to a number.
*/
if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
