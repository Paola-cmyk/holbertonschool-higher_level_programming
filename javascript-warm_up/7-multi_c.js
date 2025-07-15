#!/usr/bin/node
const args = process.argv.slice(2);
const x = parseInt(args[0], 10);
if (Number.isNaN(x) || args[0] === undefined || args[0] === '') {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
