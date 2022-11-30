/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 * absorb intervals that fall into newInterval
 */
var insert = function (intervals, newInterval) {
  const [n1, n2] = newInterval;

  let l = binarySearch(intervals, n1);
  let r = binarySearch(intervals, n2);

  const ans = [];

  for (let i = 0; i < intervals.length; i++) {
    if (i === l) {
      let leftMost = Math.min(n1, intervals[i][0]);
      let j = i;
      while (j < intervals.length) {
        if (j === r) {
          let rightMost = Math.max(n2, intervals[i][1]);
          ans.push(leftMost, rightMost);
          break;
        }
        j++;
      }
    }

    if (i < l || i > r) {
      ans.push(intervals[i]);
    }
  }
};

function binarySearch(arr, target) {
  let l = 0;
  let r = arr.length;

  while (l < r) {
    let mid = Math.floor((l + r) / 2);
    let [lmid, rmid] = arr[mid];

    if (target > lmid && target < rmid) {
      return mid;
    }
    if (target > rmid) {
      let [midl, midr] = arr[mid + 1];
      if (target < midr) {
        return mid;
      } else {
        r = mid - 1;
      }
    } else {
      l = mid + 1;
    }
  }
}
