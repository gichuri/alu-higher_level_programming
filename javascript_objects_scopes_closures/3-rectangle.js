#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
        if (w <= 0 || h <= 0 || !w || !h) return null;
        this.width = w;
        this.height = h;
    }
// create an intance method called print()
    print() {
// print the rectangle using character x

        for (let i = 0; i < this.height; i++) {
            let display = ''
            for (let j = 0; j < this.width; j++) {
                display += 'x';
            }
            console.log(display)
        }
    }
  };
module.exports = Rectangle
