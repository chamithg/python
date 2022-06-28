function findMissing(input) {
  var missing;
  var maxValue = Math.max(...input);
  var minValue = Math.min(...input);
  console.log(maxValue);
  console.log(minValue);

  for (i = minValue; i <= maxValue; i++) {
    if (input.includes(i) == false) {
      missing = i;
      break;
    }
  }

  return missing;
}

arr = [1, 2, 4, 5, 6, 7, 8, 9];

console.log(findMissing(arr));
