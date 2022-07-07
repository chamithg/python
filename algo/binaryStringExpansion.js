/* 
  Binary String Expansion
  You are given a STRING containing chars "0", "1", and "?"
  For every "?" character, either "0" or "1" can be substituted.
  Write a recursive function to return array of all valid strings with "?" chars expanded to "0" or "1". 
*/

const str1 = "1?0?";
const expected1 = ["1000", "1001", "1100", "1101"];
// output list order does not matter

/**
 * Add params if needed for recursion
 * Expands a string such that each "?" in the given string will be replaced
 * with a "0" and a "1".
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string containing to expand.
 * @returns {Array<string>} The expanded versions of the given string.
 */
function binaryStringExpansion(str, output = [], position = 0) {
  if (!str.includes("?")) {
    output.push(str);
  }

  for (position != 0 ? (i = position) : (i = 0); i < str.length; i++) {
    if (str[i] == "?") {
      let newStrA = replace(str[i], "0");
      binaryStringExpansion(newStrA, (output = []), (position = 0));
      let newStrB = replace(str[i], "1");
      binaryStringExpansion(newStrB, (output = []), (position = 0));
    }
  }

  return output;
}

console.log(binaryStringExpansion(str1));
