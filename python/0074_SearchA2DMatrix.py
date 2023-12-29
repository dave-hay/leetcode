class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = (r + l) // 2

            guess = matrix[m // COLS][m % COLS]

            if guess == target:
                return True

            if guess < target:
                l = m + 1
            else:
                r = m - 1

        return False
