function bookIndex(pages) {
  var output = pages[0].toString();
  var outputArr = [];

  for (var i = 0; i < pages.length; i++) {
    if (pages[i + 1] - pages[i] != 1) {
      outputArr.push(pages[i].toString());
    } else {
      let leftpage = pages[i];
      while (pages[i + 1] - pages[i] == 1) {
        i++;
      }
      let rightPage = pages[i];
      outputArr.push(`${leftpage}-${rightPage}`);
    }
  }
  return outputArr.join(", ");
  // Write your solution here!
}
