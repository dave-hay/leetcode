/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let min = Number.MAX_VALUE;
  let maxprofit = 0;

  for (let p of prices) {
    if (p < min) {
      min = p;
    } else if (maxprofit < p - min) {
      maxprofit = p - min;
    }
  }
  return maxprofit;
};
