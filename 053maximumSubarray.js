/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let cur = nums[0];
  let mx = nums[0];

  for (let i = 1; i < nums.length; i++) {
    cur = Math.max(nums[i], cur + nums[i]);
    mx = Math.max(mx, cur);
  }
  return mx;
};
