#!/usr/bin/node
exports.esrever = function (list) {
  const list1 = [];
  for (let a = list.length - 1; a >= 0; a--) {
    list1.push(list[a]);
  }
  return list1;
};
