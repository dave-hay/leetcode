class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isValid(self, s: str) -> bool:
        # create a hashmap key = left paren: val=right pair
        pairs = {'(': ')', '{': '}', '[': ']'}

        # create a stack to hold values and pop to match
        stack = []

        # iterate over string
        for ch in s:

            # if left paren add right pair
            if ch in pairs:
                stack.append(pairs[ch])

            # if stack empty return
            elif len(stack) == 0:
                return False
            # if right pop stack and if match continue else false
            else:
                rparen = stack.pop()
                if rparen != ch:
                    return False

        # if stack is holding right parens then false
        return len(stack) == 0
