from collections import Counter


class Optimized:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        ans = []

        for c in order:
            ans.append(c * count[c])
            count[c] = 0

        for c in count:
            ans.append(c * count[c])

        return "".join(ans)


class Naive:
    def customSortString(self, order: str, s: str) -> str:
        if len(s) == 1:
            return s
        sList = list(s)
        mp = {}
        for ch in "abcdefghijklmnopqrstuvwxyz":
            mp[ch] = float("inf")

        for i, ch in enumerate(order):
            mp[ch] = i

        sList.sort(key=lambda x: mp[x])

        return "".join(s)
