from collections import defaultdict

"""
O(n)
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force would be loop of loop
        # add counter to check divergent letters from ith
        # whole length subtracted by most common = number of changes needed
        l = 0
        ans = 0
        count = defaultdict(int)
        maxK = 0

        # as we loop we track counts and if it fits contrains then check ans
        # if too big l++
        # if too small or equal r++

        for r in range(len(s)):
            lKey = s[l]
            rKey = s[r]

            count[rKey] += 1

            maxK = max(maxK, count[rKey])

            if (r - l + 1) - maxK > k:
                count[lKey] -= 1
                l += 1

            ans = max(ans, r - l + 1)
        return ans


class Solution2:
    """
    time: O(26 * n):

    space: O(26)
    """

    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        total = 1
        alph = [0] * 26

        for right in range(len(s)):
            alph[ord(s[right]) - ord("A")] += 1

            # determine changes needed to be viable
            length = right - left + 1
            mostCommon = 0
            for count in alph:
                mostCommon = max(mostCommon, count)
            changesNeeded = length - mostCommon

            if changesNeeded <= k:
                total = max(total, length)

            else:
                # remove until can get a total
                while changesNeeded > k and left < right:
                    alph[ord(s[left]) - ord("A")] -= 1
                    left += 1
                    mostCommon = 0
                    for count in alph:
                        mostCommon = max(mostCommon, count)

                    length = right - left + 1
                    changesNeeded = length - mostCommon
        return total
