class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        nums = {val: i for i, val in enumerate(digits)}

        for i, d in enumerate(digits):
            for k in range(9, d, -1):
                if nums.get(k, 0) > i:
                    digits[i], digits[nums[k]] = digits[nums[k]], digits[i]
                    return int("".join(map(str, digits)))

        return num
