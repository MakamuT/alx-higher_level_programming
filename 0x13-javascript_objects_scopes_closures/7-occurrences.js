#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  for (let a = 0; a < list.length; a++) {
    if (list[a] === searchElement) {
      num += 1;
    }
  }
  return num;
};
