class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        """
        Do not return anything, modify matrix in-place instead.

        Just need to mark first row with 3 or first col with 3
        then if 3 mark all with 0
        """
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 3
                    matrix[0][c] = 3

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 3:
                    for i in range(COLS):
                        matrix[r][i] = 0

                    for j in range(ROWS):
                        matrix[j][c] = 0
        return matrix


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        """
        t: O(n*m)
        s: O(n+m)
        ---
        Do not return anything, modify matrix in-place instead.
        ___
        if 0 replace entire row and col with 0
        replicate, then check against it
        go thru and save locations of the place that need to be replace
        I just have to save row# and col#
        """
        # or set them to 3? then set to 0 when done
        r_coords = [1 for _ in range(ROWS)]
        c_coords = [1 for _ in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS):
                # whole row has 0s
                # whole col has 0s
                if matrix[r][c]:
                    continue
                r_coords[r] = 0
                c_coords[c] = 0

        for r in range(ROWS):
            if r_coords[r] == 0:
                for c in range(COLS):
                    matrix[r][c] = 0

        for c in range(COLS):
            if c_coords[c] == 0:
                for r in range(ROWS):
                    matrix[r][c] = 0

        return matrix
