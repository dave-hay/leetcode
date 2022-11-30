/**
 * Time complextity: O(logN)
 * Space complexity: O(1)
 */
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let l = 0;
  let h = nums.length - 1;

  while (l <= h) {
    let m = Math.floor((l + h) / 2);
    if (nums[m] === target) {
      return m;
    }
    if (nums[m] > target) {
      h = m - 1;
    } else {
      l = m + 1;
    }
  }

  return -1;
};
