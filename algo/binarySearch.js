// Implement binarySearch(arr, target), a function that takes in two arguments -
// an array (of integers, sorted) to search and a target (an integer) to search for.
// Have the function return true if the item is present in the array and false otherwise.

// This can be done with a linear search (i.e. checking each item in the
// array one by one), but this is slow - O(n) time. We can do it much faster -
// specifically, O(log n) time - as long as we do it carefully.

// needs some other parameters to work properly... probably?

function binarySearch(input, target) {
  if (input[0] > target || input[input.length - 1] < target) {
    return false;
  }
  if (input.length < 5) {
    for (var i = 0; i < input.length; i++) {
      if (input[i] == target) {
        return true;
      }
    }
    return false;
  } else {
    var midpoint = Math.floor(input.length / 2);

    if (target <= input[midpoint]) {
      var arr1 = input.slice(0, midpoint);
      return binarySearch(arr1, target);
    } else {
      var arr2 = input.slice(midpoint);
      return binarySearch(arr2, target);
    }
  }
}

var input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 17, 18, 20, 21, 22];
var target = 4;

console.log(binarySearch(input, target));
