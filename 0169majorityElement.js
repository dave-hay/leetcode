/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  if (!nums.length) return nums[0];

  const majority = Math.ceil(nums.length / 2);
  const map = {};

  for (let i = 0; i < nums.length; i++) {
    if (!map[nums[i]]) {
      map[nums[i]] = 0;
    }

    map[nums[i]]++;

    if (map[nums[i]] >= majority) {
      return nums[i];
    }
  }
};
