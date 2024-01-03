class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        if len(bank) == 1:
            return 0

        res = prev = 0
        for cur in bank:
            freq = 0

            for c in cur:
                if c == "1":
                    freq += 1

            if freq > 0:
                res += prev * freq
                prev = freq

        return res
