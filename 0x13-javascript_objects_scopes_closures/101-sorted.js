#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

for (const n in dict) {
  if (!newDict[dict[n]]) {
    newDict[dict[n]] = [];
  }
  newDict[dict[n]].push(n);
}

console.log(newDict);
