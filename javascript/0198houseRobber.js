/**
 * @param {number[]} nums
 * @return {number}
 optimal val = max money;
 future dependent on prev;
 dp(i) = nums[i] + dp(i + 2), dp(i + 1)
 */
var rob = function (nums) {
  if (nums.length < 2) return nums[0];
  const res = Array(nums.length).fill(0);
  res[0] = nums[0];
  res[1] = nums[0] > nums[1] ? nums[0] : nums[1];
  for (let i = 2; i < nums.length; i++) {
    const opt1 = res[i - 2] + nums[i];
    const opt2 = res[i - 1];
    res[i] = Math.max(opt1, opt2);
  }
  return res[nums.length - 1];
};
