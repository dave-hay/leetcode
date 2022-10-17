/**
 * // Definition for a Node.
 * function Node(val, neighbors) {
 *    this.val = val === undefined ? 0 : val;
 *    this.neighbors = neighbors === undefined ? [] : neighbors;
 * };
 */

/**
 * @param {Node} node
 * @return {Node}
 */

var cloneGraph = function (n) {
  if (!n) return n;
  const seen = {};

  const dfs = (node) => {
    if (!node) return node;
    if (node.val in seen) return seen[node.val];

    const clone = new Node(node.val);
    seen[node.val] = clone;

    if (node.neighbors.length > 0) {
      for (let n of node.neighbors) {
        const nbor = dfs(n);
        clone.neighbors.push(nbor);
      }
    }
    return clone;
  };
  return dfs(n);
};
