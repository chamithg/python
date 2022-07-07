var phone = {
  1: "_,@",
  2: "ABC",
  3: "DEF",
  4: "GHI",
  5: "JKL",
  6: "MNO",
  7: "PQRS",
  8: "TUV",
  9: "WXYZ",
  0: " ",
};

function telephoneNumbers(input, output = [], position = 0, partial = "") {
  if (position >= input.length) {
    output.push(partial);
  } else {
    for (var i = 0; i < phone[input[position]].length; i++) {
      let char = phone[input[position]][i];
      let new_partial = partial + char;
      telephoneNumbers(input, output, position + 1, new_partial);
    }
  }

  return output;
}

console.log(telephoneNumbers("123456"));
