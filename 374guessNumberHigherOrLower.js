/**
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 * 			      1 if num is lower than the picked number
 *               otherwise return 0
 * var guess = function(num) {}
 */

/**
 * @param {number} n - largest possible value
 * @return {number}
 * binary search
 */
var guessNumber = function (n) {
  if (n === 1) return 1;

  let high = n;
  let low = 1;
  while (low < high) {
    let mid = Math.floor((low + high) / 2);
    let resp = guess(mid);

    if (resp === -1) { // mid is too big
      high = mid - 1;
    }
    if (resp === 1) { // mid is too small
      low = mid + 1;
    }
    if (resp === 0) {
      return mid;
    }
  }
  return high;
};
