/** Set
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  let longest = 0;
  let set = new Set(nums);

  for (let n of set) {
    if (!set.has(n - 1)) {
      let cur = n;
      let streak = 1;

      while (set.has(cur + 1)) {
        cur++;
        streak++;
      }
      longest = Math.max(longest, streak);
    }
  }
  return longest;
};

/** Sorted
 * Time Complexity: O(Nlog(N))
 * Space Complexity: O(1) or O(N) if can't modify input
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  if (nums.length < 2) return nums.length;
  nums.sort((a, b) => a - b);

  let longest = 1;
  let cur = 1;

  for (let i = 1; i < nums.length; i++) {
    if (nums[i - 1] !== nums[i]) {
      if (nums[i - 1] === nums[i] - 1) {
        cur += 1;
      } else {
        cur = 1;
      }
      if (cur > longest) {
        longest = cur;
      }
    }
  }
  return longest;
};
