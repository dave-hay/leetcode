/**
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  if (s.length < 2) return true;

  const isalnum = (ch) => ("a" <= ch && ch <= "z") || ("0" <= ch && ch <= "9");
  s = s.toLowerCase();

  let l = 0;
  let h = s.length;
  while (l < h) {
    while (!isalnum(s[l]) && l < h) {
      l++;
    }
    while (!isalnum(s[h]) && l < h) {
      h--;
    }
    if (s[l] !== s[h]) return false;
    l++;
    h--;
  }
  return true;
};

/**
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  if (s.length < 2) return true;
  let sArray = s.toLowerCase().split("");

  let filtered = sArray.filter((ch) => {
    return ("a" <= ch && ch <= "z") || ("0" <= ch && ch <= "9");
  });

  let i = 0;
  let j = filtered.length - 1;
  while (i < j) {
    if (filtered[i] !== filtered[j]) return false;
    i++;
    j--;
  }
  return true;
};
