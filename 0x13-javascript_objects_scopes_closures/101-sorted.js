#!/usr/bin/node
const dict = require('./101-data').dict;
const newDictionary = {};

for (const key in dict) {
  if (typeof (newDictionary[dict[key]]) === 'undefined') {
    newDictionary[dict[key]] = [];
  }
  newDictionary[dict[key]].push(key);
}

console.log(newDictionary);
