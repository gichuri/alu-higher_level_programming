#!/usr/bin/node
exports.converter = function (base) {
  return (a) => a.tostring(base);
};
