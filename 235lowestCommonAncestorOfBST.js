/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
// inOrder traversal?
// once the ans has been hit keep going to parent until it's the same
// since binary tree know if smaller traverse left and bigger go right
var lowestCommonAncestor = function (root, p, q) {
  let curVal = root.val;
  let pVal = p.val;
  let qVal = q.val;

  if (curVal > pVal && curVal > qVal) {
    return lowestCommonAncestor(root.left, p, q);
  } else if (curVal < pVal && curVal < qVal) {
    return lowestCommonAncestor(root.right, p, q);
  } else {
    return curVal;
  }
};
