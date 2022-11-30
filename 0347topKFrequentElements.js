/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  if (nums.length === k) return nums;

  /** Step 1
   * loop over nums to get frequency
   * map = {num[i]: count}
   */
  let map = {};
  for (let n of nums) {
    map[n] = n in map ? map[n] + 1 : 1;
  }

  /** Step 2
   * store key/num[i] in a matrix indexed by count
   * matrix size is + 1 since count will be at least 1
   */
  let matrix = Array.from({ length: nums.length + 1 }, () => []);
  for (let m in map) {
    matrix[map[m]].push(m);
  }

  /** Step 3
   * loop over matrix in descending order adding to answer array until size k
   * need explicit skip if matrix index is empty
   */
  let ans = [];
  for (let i = matrix.length - 1; i >= 0; i--) {
    if (matrix[i].length > 0) {
      matrix[i].forEach((n) => ans.push(n));
      if (ans.length === k) {
        return ans;
      }
    }
  }
};
