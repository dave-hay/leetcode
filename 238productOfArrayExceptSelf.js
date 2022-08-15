/**
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  // get total product
  let product = 0;
  let zeroCount = 0;

  for (let n of nums) {
    if (n !== 0) product = product ? product * n : 1 * n;
    if (n === 0) zeroCount++;
  }

  let ans = Array(nums.length).fill(0);
  if (zeroCount > 1) return ans; // if more than one zero return zero'd array

  if (zeroCount === 1) {
    for (let i = 0; i < nums.length; i++) {
      // if nums[i] not 0 ignore
      // if nums[i] is 0 add product
      if (nums[i] === 0) ans[i] = product;
    }
  } else {
    for (let i = 0; i < nums.length; i++) {
      ans[i] = product / nums[i];
    }
  }
  return ans;
};
