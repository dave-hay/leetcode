from collections import defaultdict, deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        node_list = []
        q = deque([(root, 0, 0)])  # Node, row, column

        while q:
            node, row, col = q.popleft()
            if node:
                node_list.append((col, row, node.val))
                q.append((node.left, row + 1, col - 1))
                q.append((node.right, row + 1, col + 1))

        node_list.sort()  # Sort by column, then row, then value

        result = defaultdict(list)
        for col, row, val in node_list:
            result[col].append(val)

        return [result[x] for x in sorted(result)]
