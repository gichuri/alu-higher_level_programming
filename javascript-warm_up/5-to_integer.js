#!/usr/bin/node
const args = process.argv;
if (Number(args[2]) != NaN) {
  console.log('My number:', Number(args[2]));
} else if ('My number:', Number(args[2]) === NaN) {
  console.log('Not a number');
} else {
    console.log('Not a number');
}
