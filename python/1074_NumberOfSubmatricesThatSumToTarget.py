class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        rows, cols = len(matrix), len(matrix[0])
        # Compute prefix sums for each row
        for r in range(rows):
            for c in range(1, cols):
                matrix[r][c] += matrix[r][c - 1]

        count = 0
        # Iterate over all pairs of columns
        for left in range(cols):
            for right in range(left, cols):
                sums = {0: 1}
                curr_sum = 0
                # Count subarrays with sum equal to target
                for r in range(rows):
                    curr_sum += matrix[r][right] - (
                        matrix[r][left - 1] if left > 0 else 0
                    )
                    count += sums.get(curr_sum - target, 0)
                    sums[curr_sum] = sums.get(curr_sum, 0) + 1
        return count
