function intersection(arr1, arr2) {
  var result1 = {};
  var result2 = {};
  var result3 = {};
  for (var i = 0; i < arr1.length; i++) {
    if (arr1[i] in result1) {
      result1[arr1[i]] += 1;
    } else {
      result1[arr1[i]] = 1;
    }
  }
  for (var i = 0; i < arr2.length; i++) {
    if (arr2[i] in result2) {
      result2[arr2[i]] += 1;
    } else {
      result2[arr2[i]] = 1;
    }
  }
  for (let key in result1) {
    if (result2[key]) {
      if (result1[key] > result2[key]) {
        result3.push(result2(key));
      }
    }
  }
  console.log(result3);
}

arr1 = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5];
arr2 = [2, 2, 3, 3, 6, 6, 7, 7, 7, 8, 9];

intersection(arr1, arr2);
