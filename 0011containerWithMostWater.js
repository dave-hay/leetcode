/**
 * Time Complexity: O(n) single pass
 * Space Complexity: O(1) constant space
 */
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let left = 0;
  let right = height.length - 1;

  let ans = 0;
  while (left < right) {
    let guess = Math.min(height[left], height[right]) * (right - left);
    if (guess > ans) {
      ans = guess;
    }
    // what to do if height equal?
    if (height[left] > height[right]) {
      right--;
    } else {
      left++;
    }
  }
  return ans;
};
