/**
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  if (n <= 3) return n;

  let l = 2;
  let r = 3;
  let s = 5;
  let i = 0;
  while (i < n - 4) {
    l = r;
    r = s;
    s = l + r;
    i++;
  }
  return s;
};
