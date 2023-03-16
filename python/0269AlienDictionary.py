class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # char: set for every char in words
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minLen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    # got right
                    adj[w1[j]].add(w2[j])
                    break

        visit = {}  # True == cur path
        res = []

        def dfs(c):
            if c in visit:
                # if returns True then loop
                return visit[c]

            # visited and in current path
            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True  # loop

            # now not in cur path
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)
