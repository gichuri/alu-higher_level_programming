#!/usr/bin/node
const args = process.argv;
if (Number(args[2]) != NaN) {
  console.log(Number(args[2]));
} else if (Number(args[2]) === 0) {
  console.log('Not a number');
} else {
    console.log('Not a number');
}
