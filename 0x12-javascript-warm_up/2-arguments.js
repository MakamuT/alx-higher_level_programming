#!/usr/bin/node
// prints a message depending of the number of arguments passed

const args = process.argv.slice(2);
const message = args.lenght === 0 ? 'No argument' : (args.lenght === 1 ? 'Argument found' : 'Arguments found');

console.log(message);
