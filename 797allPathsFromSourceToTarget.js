/**
 * Depth First Search
 * Time: O(2^V * V)
 * Space: O(V)
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTargetDFS = function(graph) {
  if (!graph || graph.length === 0) {
    return []
  }
  // given a adjacency list
  const res = [];
  const cur = []

  function dfs(node) {
    cur.push(node)
    if (node === graph.length - 1) {
      res.push(Array.from(cur))
      return
    }

    const next = graph[node]
    for (let n of next) {
      dfs(n)
      cur.pop()
    }
  }

  dfs(0)
  return res
};

