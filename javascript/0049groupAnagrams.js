/**
 * Time Complexity: O(NK)
 * Space Complexity: O(NK)
 *
 * N = length of strs array
 * K = max length of string inside strs
 */

/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  if (strs.length === 1) return [strs]; // if only one value already have ans

  const map = {};

  for (let s of strs) {
    let alph = Array(26).fill(0);

    for (let c of s) {
      let alphIndex = c.charCodeAt(0) - "a".charCodeAt(0);
      alph[alphIndex]++; // increment not binary prevent edge case e.g. 'hello' v 'helo'
    }

    if (map[alph]) {
      map[alph].push(s);
    } else {
      map[alph] = [s];
    }
  }

  return Object.values(map);
};
