/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  let res = [];
  nums.sort();
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 0) break;
    if (i === 0 || nums[i - 1] != nums[i]) {
      twoSum(nums, i, res);
    }
  }
  return res;
};

const twoSum = (nums, i, res) => {
  let seen = new Set();
  let j = i + 1;

  while (j < nums.length) {
    let comp = -nums[i] - nums[j];
    if (seen.has(comp)) {
      res.push([nums[i], nums[j], comp]);
      while (j + 1 < nums.length && nums[j] === nums[j + 1]) {
        j++;
      }
    }
    seen.add(nums[j]);
    j++;
  }
};
