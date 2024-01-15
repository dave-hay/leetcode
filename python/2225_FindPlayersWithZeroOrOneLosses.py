class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        mp = {}
        res = [[], []]

        for w, l in matches:
            if w not in mp:
                mp[w] = 0

            mp[l] = mp.get(l, 0) + 1

        for player, losses in mp.items():
            if losses > 1:
                continue

            res[losses].append(player)

        res[0].sort()
        res[1].sort()

        return res
