class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        arr = ["0"] * len(s)
        arr[-1] = "1"
        ones = -1

        for i in s:
            if i == "1":
                ones += 1

        for i in range(ones):
            arr[i] = "1"

        return "".join(arr)
