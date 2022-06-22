// Given two arrays, return a new array containing the the items from each array interleaved - if array A contains {1, 2, 3] and array B contains [44, 55, 66], return an array containing [1, 44, 2, 55, 3, 66]. If one array is longer than the other, the extra items will just be at the end of the array - given an array containing [7, 8, 9] and [1, 2, 3, 4, 5, 6], return an array containing [7, 1, 8, 2, 9, 3, 4, 5, 6]

export function interleaveArrays(arrayA, arrayB) {
  var outputArray = [];
  var longest;

  if (arrayA.length < arrayB.length) {
    longest = arrayB.length;
  } else {
    longest = arrayA.length;
  }
  for (var i = 0; i < longest; i++) {
    if (arrayA[i]) {
      outputArray.push(arrayA[i]);
    }
    if (arrayB[i]) {
      outputArray.push(arrayB[i]);
    }
  }
  return outputArray;
}
