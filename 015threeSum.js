/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  let ans = [];
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 0) {
      break;
    } else if (i === 0 || nums[i] != nums[i - 1]) {
      twoSum(i, ans, nums);
    }
  }
  return ans;
};

const twoSum = (i, ans, nums) => {
  let lo = i + 1;
  let hi = nums.length - 1;

  while (lo < hi) {
    let sum = nums[i] + nums[lo] + nums[hi];
    if (sum > 0) {
      hi--;
    } else if (sum < 0) {
      lo++;
    } else {
      ans.push([nums[i], nums[lo], nums[hi]]);
      lo++;
      hi--;

      while (lo < hi && nums[lo] == nums[lo - 1]) {
        lo++;
      }
    }
  }
};
