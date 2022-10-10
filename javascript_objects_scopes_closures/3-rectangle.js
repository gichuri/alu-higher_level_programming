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
    double() {
        // multiply width and height by 2
        this.height*=2;
        this.width*=2;
    }
    rotate() {
        [this.width, this.height] = [this.height, this.width];
    }
  };
module.exports = Rectangle
