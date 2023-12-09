class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0

        while i < len(word) and j < len(abbr):
            if abbr[i].isalpha():
                # must be same character
                if abbr[j] != word[i]:
                    return False

                # increment
                i += 1
                j += 1
            else:
                # is num as only nums or letters passed
                if abbr[j] == "0":
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1

                i += num

        return i == len(word) and j == len(abbr)
