/**
 * Time complexity: O(log N)
 * Space complexity: O(1)
 */
/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function (x) {
  if (x < 2) return x;

  let low = 2;
  let high = Math.floor(x / 2);

  while (low <= high) {
    let mid = Math.floor(low + (high - low) / 2);
    let guess = mid * mid;

    if (guess > x) {
      high = mid - 1;
    } else if (guess < x) {
      low = mid + 1;
    } else {
      return mid;
    }
  }
  return high;
};
