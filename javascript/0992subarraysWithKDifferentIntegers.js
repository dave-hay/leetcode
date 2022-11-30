/**
 * @param {number[]} nums
 * @param {number} k === diff ints needed
 * @return {number} num of good subarrays
 */
var subarraysWithKDistinct = function (nums, k) {
  return atMostK(nums, k) - atMostK(nums, k - 1);
};

function atMostK(a, k) {
  const count = {};
  let res = 0;
  let i = 0;

  for (let j = 0; j < a.length; j++) {
    // new unique element, set up map and decrement k
    if (!count[a[j]]) {
      count[a[j]] = 0;
      k--;
    }
    count[a[j]]++; // new or cur key increments
    // keep adding keys until one too many
    while (k < 0) {
      count[a[i]]--; //
      if (count[a[i]] === 0) {
        k++;
      }
      i++;
    }
    res += j - i + 1;
  }
  return res;
}
