function arrayOddOccurances(arr) {
  var obj = {};
  for (var i = 0; i < arr.length; i++) {
    if (Object.keys(obj).indexOf(arr[i]) < 0) {
      obj[arr[i]] = 1;
    } else {
      obj[arr[i]] += 1;
    }
  }
  for (var key in obj) {
    if (obj[key] % 2 == 1) {
      return key;
    }
  }
  console.log(obj);

  return false;
}

arrayOddOccurances([26, 34, 26]);
