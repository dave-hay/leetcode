class Solution:
    """
    naive: O(2^n)
    ---
    n = total groups
    p = total parenthesis

    ---
    so it's called O(2^p) ~= O(2^n)
    ---
    # but stops if l > r
    so what would new worst case be?
    3
    (()) )
    n - 1 then on last try it is not correct
    or (2n - 2)
    O(2)


    """

    def __init__(self):
        self.res = []

    def generateParenthesis(self, n: int) -> list[str]:
        def dp(left, right, string):
            if left == n and right == n:
                self.res.append(string)
                return

            # place new open
            if left < n:
                dp(left + 1, right, string + "(")
            if right < left:
                dp(left, right + 1, string + ")")

        # have to place at least one left
        dp(1, 0, "(")
        return self.res
