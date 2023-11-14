#!/usr/bin/node

let number = 0;

exports.logMe = function (item) {
  console.log(`${number++}: ${item}`);
};
