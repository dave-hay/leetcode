from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = defaultdict(int)

        for num in arr:
            seen[num] += 1

        occurances = set()
        for oc in seen.values():
            if oc in occurances:
                return False
            occurances.add(oc)
        return True
