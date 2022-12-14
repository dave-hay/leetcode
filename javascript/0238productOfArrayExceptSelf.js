/**
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const res = [];

  let product = 1;

  for (let i = 0; i < nums.length; i++) {
    res[i] = product;
    product *= nums[i];
  }
  product = 1;
  for (let j = nums.length - 1; j >= 0; j--) {
    res[j] *= product;
    product *= nums[j];
  }

  return res;
};

/**
 * Verbose solution
 */
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  let left = Array(nums.length);

  let product = 1;
  for (let i = 0; i < nums.length; i++) {
    left[i] = product;
    product *= nums[i];
  }

  product = 1;
  let right = Array(nums.length);
  for (let i = nums.length - 1; i >= 0; i--) {
    right[i] = product;
    product *= nums[i];
  }

  let ans = Array(nums.length);
  for (let i = 0; i < nums.length; i++) {
    ans[i] = left[i] * right[i];
  }
  return ans;
};
