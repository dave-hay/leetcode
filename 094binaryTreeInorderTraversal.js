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
 * @return {number[]}
 */

class Idk {
  constructor() {
    this.nums = [];
  }

  traverse(r) {
    if (!r) return null;
    this.traverse(r.left);
    this.nums.push(r.val);
    this.traverse(r.right);
  }
}

var inorderTraversal = function (root) {
  if (!root) return [];
  const obj = new Idk();
  obj.traverse(root);

  return obj.nums;
};
