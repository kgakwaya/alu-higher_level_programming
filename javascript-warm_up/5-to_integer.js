#!/usr/bin/node

const args = process.argv[2];
const number = parseInt(args);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}

