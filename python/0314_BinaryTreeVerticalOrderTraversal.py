# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque


class SolutionA:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        time: O(n)
        space: O(n)
        algo: Level-order traversal (BFS)
        data structure: map, queue
        ---
        Store {col: nodeVals[]}.
        Track min and max values of cols.
        return node in order from lo to hi
        """
        if not root:
            return []

        nodes = defaultdict(list)
        q = deque([(root, 0)])
        lo = hi = 0

        while q:
            node, col = q.popleft()

            if not node:
                continue

            nodes[col].append(node.val)

            lo = min(col, lo)
            hi = max(col, hi)
            q.append((node.left, col - 1))
            q.append((node.right, col + 1))

        return [nodes[col] for col in range(lo, hi + 1)]


class SolutionB:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        time: O(n log n)
        space: O(n)
        ---
        Less efficient using sort
        """
        nodes = defaultdict(list)
        q = deque([(root, 0)])

        while q:
            node, col = q.popleft()

            if not node:
                continue

            nodes[col].append(node.val)

            q.append((node.left, col - 1))
            q.append((node.right, col + 1))

        order = sorted(nodes)
        return [nodes[col] for col in order]
