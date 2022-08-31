# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def lcaIterative(self, root, p, q):
        # Get values of p and q
        p_val = p.val
        q_val = q.val

        node = root

        # Traverse the tree
        while node:
            parent_val = node.val

            # If p and q > parent
            if p_val > parent_val and q_val > parent_val:
                node = node.right

            # If p and q < parent
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node

    def lcaRecursive(self, root, p, q):

        # Get node values
        parent_val = root.val
        p_val = p.val
        q_val = q.val

        # If p and q > parent
        if p_val > parent_val and q_val > parent_val:
            return self.lcaRecursive(root.right, p, q)
        # If p and q < parent
        elif p_val < parent_val and q_val < parent_val:
            return self.lcaRecursive(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root
