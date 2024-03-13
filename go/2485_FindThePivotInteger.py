class Solution:
    def pivotInteger(self, n: int) -> int:
        sm = lambda n: ((n * (n + 1)) // 2)

        l, r = 1, n

        mid = -1
        while l <= r:
            mid = (l + r) // 2

            left_sum = sm(n) - sm(mid - 1)
            right_sum = sm(mid)
            if left_sum == right_sum:
                return mid

            if left_sum > right_sum:
                l = mid + 1
            else:
                r = mid - 1

        return -1
