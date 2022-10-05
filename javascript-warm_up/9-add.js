#!/usr/bin/node
const args = process.argv;
function add(a, b){
  if (isNaN(args[2])){
    console.log('NaN');
  } else if (isNaN(args[3])) {
    console.log('NaN');
  } else {
    sum = args[2] + args[3];
    console.log(sum);
  }
}
