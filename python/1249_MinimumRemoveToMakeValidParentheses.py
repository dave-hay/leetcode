class Solution2:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        open_count = 0

        # Forward pass to remove extra ')'
        for i in range(len(s)):
            if s[i] == "(":
                open_count += 1
            elif s[i] == ")":
                if open_count == 0:
                    s[i] = ""
                else:
                    open_count -= 1

        # Reverse pass to remove extra '('
        for i in range(len(s) - 1, -1, -1):
            if open_count > 0 and s[i] == "(":
                s[i] = ""
                open_count -= 1

        return "".join(s)


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        - Use a stack to keep track of the indices of open parentheses.
        - Traverse the string, pushing the index of each '(' onto the stack.
        - When encountering a ')', pop from the stack if it's not empty (which means there's a matching '(').
        - If the stack is empty, this ')' is extra and should be removed.
        - After the traversal, any indices remaining in the stack represent unmatched '(' and should also be removed.
        """
        stack = []
        s = list(s)

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        while stack:
            s[stack.pop()] = ""
        return "".join(s)
