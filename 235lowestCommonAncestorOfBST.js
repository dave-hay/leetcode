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
 * Time Complexity: O(N) - Where N is the height of the tree
 * Space Complexity: O(1)
 */
var lowestCommonAncestorIterative = function (root, p, q) {
  const pVal = p.val;
  const qVal = q.val;

  let node = root;

  while (node) {
    let nVal = node.val;

    if (nVal > pVal && nVal > qVal) {
      node = node.left;
      continue;
    }

    if (nVal < pVal && nVal < qVal) {
      node = node.right;
      continue;
    }

    return node;
  }
};

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 * Time Complexity: O(N) - Where N is the height of the tree
 * Space Complexity: O(N) - Recusive call stack
 */
var lowestCommonAncestorRecursive = function (root, p, q) {
  let curVal = root.val;
  let pVal = p.val;
  let qVal = q.val;

  if (curVal > pVal && curVal > qVal) {
    return lowestCommonAncestorRecursive(root.left, p, q);
  } else if (curVal < pVal && curVal < qVal) {
    return lowestCommonAncestorRecursive(root.right, p, q);
  } else {
    return curVal;
  }
};
