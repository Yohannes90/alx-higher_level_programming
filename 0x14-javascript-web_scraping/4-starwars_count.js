#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const results = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      const chars = (results[i].characters);
      for (let j = 0; j < chars.length; j++) {
        if (chars[j].endsWith('18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
