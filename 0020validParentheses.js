/** Time complexity: O(n)
 *   traverse every char in string
 *   push/pop on a stack takes O(1)
 *
 *  Space complexity: O(n)
 *    worst case end up pushing all the brackets onto the stack. e.g. ((((((((((.
 */

/**
 * @param {string} s
 * @return {boolean}
 * '()[]{}'
 */
var isValid = function (s) {
  const compliment = { "(": ")", "[": "]", "{": "}" };
  const stack = [];

  for (let c of s) {
    if (c in compliment) {
      stack.push(compliment[c]); // add closing to stack
    } else {
      let close = stack.pop();
      if (close !== c) return false;
    }
  }

  return stack.length === 0;
};
