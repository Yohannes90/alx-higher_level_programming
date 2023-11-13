#!/usr/bin/node

const argv = process.argv;

function add (num1, num2) {
  return num1 + num2;
}
console.log(add(Number(argv[2]), Number(argv[3])));
