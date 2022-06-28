function sumOfNestedArrays(input) {
  var total = 0;
  for (var i = 0; i < input.length; i++) {
    if (Array.isArray(input[i])) {
      total += sumOfNestedArrays(input[i]);
    } else {
      total += input[i];
    }
  }
  return total;
}
console.log(sumOfNestedArrays([1, 2, 3, 4, 5])); // returns 15
console.log(sumOfNestedArrays([1, 2, 3, 4, [1, 1, 2]])); // returns 14
console.log(
  sumOfNestedArrays([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
  ])
); // returns 36
console.log(
  sumOfNestedArrays([1, [1, 2, 3], [7, [5, 4, 1]], [21, -7, 1], [1, 13, 131]])
);
