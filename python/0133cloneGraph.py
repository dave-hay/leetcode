"""
Time Complexity: O(Nodes + Edges),
Space Complexity: O(N).
    Hash map of visited
    Recursion stack O(H) where H = height of the graph.
    Overall, the space complexity would be O(N).
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        clone = Node(node.val, [])

        self.visited[node] = clone

        if node.neighbors:
            clone.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone


"""
dfs
"""


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        seen = {}

        def dfs(cur):
            if not cur:
                return cur

            cpy = Node(cur.val)
            seen[cur.val] = cpy

            neighbors = cur.neighbors

            for n in neighbors:
                if n.val in seen:
                    cpy.neighbors.append(seen[n.val])
                else:
                    cpy.neighbors.append(dfs(n))
            return cpy

        return dfs(node)
