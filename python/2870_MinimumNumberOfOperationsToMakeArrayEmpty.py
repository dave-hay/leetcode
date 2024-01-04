from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for c in counter.values():
            if c == 1:
                return -1
            ans += ceil(c / 3)
        return ans


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mp = Counter(nums)
        res = 0

        for freq in mp.values():
            if freq == 1:
                return -1

            cur = freq
            while cur:
                if cur % 3 == 0:
                    res += int(cur / 3)
                    break
                elif cur % 3 == 2:
                    res += int(cur / 3) + 1
                    break
                else:
                    cur -= 2
                    res += 1

        return res
