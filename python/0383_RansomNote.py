class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        dict: {char: count}
        array of size 26
        """

        seen = {}

        for char in magazine:
            seen[char] = seen.get(char, 0) + 1

        for char in ransomNote:
            if char not in seen:
                return False

            if seen[char] == 0:
                return False

            seen[char] -= 1

        return True
