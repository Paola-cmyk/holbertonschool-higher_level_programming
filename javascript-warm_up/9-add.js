#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const args = process.argv.slice(2);
const a = parseInt(args[0], 10);
const b = parseInt(args[1], 10);

console.log(add(a, b));
