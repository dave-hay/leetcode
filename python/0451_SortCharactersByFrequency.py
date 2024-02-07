from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        n: length of string
        k: # of unique chars
        space: O(n + k log k)
        time: O(n)
        """
        counts = Counter(s)

        arr = []

        for c, freq in counts.items():
            arr.append((c, freq))

        arr.sort(key=lambda x: -x[1])

        res = ""
        for c, freq in arr:
            res += c * freq

        return res


class Solution:
    """
    space: O(n)
    time: O(n)
    """

    def frequencySort(self, s: str) -> str:
        # Counting frequency of each character
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Creating buckets for frequencies
        buckets = [[] for _ in range(len(s) + 1)]
        for char, f in freq.items():
            buckets[f].append(char)

        # Building the result string from buckets
        result = []
        for i in range(len(s), 0, -1):  # Start from the highest possible frequency
            for char in buckets[i]:
                result.append(char * i)  # Append character i times

        return "".join(result)
