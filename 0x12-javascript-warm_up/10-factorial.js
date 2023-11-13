#!/usr/bin/node

const argv = process.argv;

function factorial (num) {
  if (num === 0 || !num) {
    return 1;
  }
  return num * factorial(--num);
}
console.log(factorial(Number(argv[2])));
