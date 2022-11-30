/**
 * Time complexity: O(n)
 * Space complexity: O(1) Although we do use extra space, the space complexity
 * is O(1) because the table's size stays constant no matter how large n is.
 */
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  let sArr = Array(26).fill(0);
  let tArr = Array(26).fill(0);
  for (let i = 0; i < s.length; i++) {
    let sval = s[i].charCodeAt(0) - "a".charCodeAt(0);
    let tval = t[i].charCodeAt(0) - "a".charCodeAt(0);
    sArr[sval]++;
    tArr[tval]++;
  }

  for (let i = 0; i < sArr.length; i++) {
    if (sArr[i] !== tArr[i]) return false;
  }
  return true;
};
