#!/usr/bin/node
const args = process.argv;
if (isNaN(Number(args[2]))) {
    console.log('Missing size');
} else {
    for (i = 0; i < Number(args[2]); i++) {
    let row = ''
      for (j = 0; j < Number(args[2]); j++) {
      row+= 'X';
      }
console.log(row+'')
    }
}
