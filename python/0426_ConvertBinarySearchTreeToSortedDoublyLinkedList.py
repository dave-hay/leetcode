"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class SolutionRecursive:
    def treeToDoublyList(self, root):
        if not root:
            return None

        first, last = None, None

        def in_order(node):
            nonlocal first, last
            if node:
                # In-order traversal: left -> node -> right
                in_order(node.left)

                # Link the previous node (last) with the current node
                if last:
                    last.right = node
                    node.left = last
                else:
                    # Initialize the first node
                    first = node

                # Mark this node as the last node
                last = node

                in_order(node.right)

        in_order(root)

        # Close the circular doubly linked list
        last.right = first
        first.left = last

        return first


class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return None

        stack = []
        current = root
        first, last = None, None

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            # Link the current node with the last node in the list
            if last:
                last.right = current
                current.left = last
            else:
                first = current

            last = current
            current = current.right

        # Make the list circular
        last.right = first
        first.left = last

        return first
