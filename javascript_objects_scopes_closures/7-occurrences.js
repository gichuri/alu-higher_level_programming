#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const element of list) {
    if (element === searchElement) { count++; }
  }
  return count;

  // loop through each element using for loop
  // count the number of occurences for each element in question
};
