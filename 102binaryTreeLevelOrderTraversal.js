/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function (root) {
  let ans = [];
  if (!root) return ans;

  function traverse(head, lvl) {
    if (!head) return;
    if (ans.length === lvl) ans.push([]);
    ans[lvl].push(head.val);
    traverse(head.left, lvl + 1);
    traverse(head.right, lvl + 1);
  }
  traverse(root, 0);
  return ans;
};
