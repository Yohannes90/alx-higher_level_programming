#!/usr/bin/node

const argv = process.argv;

if (argv.length <= 3) {
  console.log(0);
} else {
  const args = argv.slice(2, argv.length).sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
