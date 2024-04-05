class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and (
                (char.isupper() and stack[-1] == char.lower())
                or (char.islower() and stack[-1] == char.upper())
            ):
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
