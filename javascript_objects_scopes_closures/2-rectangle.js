#!/usr/bin/node
module.imports = class Rectangle {
  constructor (w, h) {
    if (w || h <= 0) {
      Object.create(null);
    } else {
      this.height = h;
      this.width = w;
    }
  }
};
