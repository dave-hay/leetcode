class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        1 -> numRows each own row
        r+1 until r == numRows - 1
        then r - 1 col + 1 until r == 0
        """
        if numRows == 1 or numRows >= len(s):
            return s

        mp = {}

        r = 0
        step = -1

        for c in s:
            mp[r] = mp.get(r, "") + c

            if r == 0 or r == numRows - 1:
                step *= -1

            r += step

        # res = ''
        # for v in mp.values():
        #     res += v
        return "".join(mp.values())
