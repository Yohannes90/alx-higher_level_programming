#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const todos = JSON.parse(body);
    const completed = todos.filter(task => task.completed).forEach((todo) => {
      completed[todo.userId] === undefined ? completed[todo.userId] = 1 : completed[todo.userId] += 1;
    });
    console.log(completed);
  }
});
