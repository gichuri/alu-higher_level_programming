#!/usr/bin/node
const parentsquare = require('./5-square');

class Square extends parentsquare {
  charprint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}
module.exports = square;
