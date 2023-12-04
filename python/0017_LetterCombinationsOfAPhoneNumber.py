class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtracking(i, curString):
            """
            i: index in digits
            curString
            """
            # basecase
            if len(curString) == len(digits):
                res.append(curString)
                return

            # loop over possible combos
            for c in digitMap[digits[i]]:
                backtracking(i + 1, curString + c)

        backtracking(0, "")
        return res
