#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w <= 0 ) || (h <= 0) || !h || !w) {
      return this;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let row = '';
      for (let b = 0; b < this.width; b++) {
        row += 'X';
      }
      console.log(row);
    }
  }
};
