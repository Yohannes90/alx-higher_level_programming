#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.foreach(char => {
      request(char, (error, response, body) => {
        console.log(error || JSON.parse(body).name);
      });
    });
  }
});
