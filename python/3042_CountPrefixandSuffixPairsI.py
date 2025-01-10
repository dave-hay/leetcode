from typing import List


class Solution:
    """
    hmm
    could try words[0] against words[1] -> words[n]
    this would take n^2 * m time
    but since words.length <= 50 would be constant
    ---
    likely want a faster solution
    well 26 characters
    create a trie?
    """

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            if len(str1) > len(str2):
                return False
            # check slices
            # str1List, str2List = list(str1), list(str2)
            isPrefix = str1 == str2[: len(str1)]
            isSuffix = str1 == str2[len(str2) - len(str1) :]
            return isPrefix and isSuffix

        count = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                count += int(isPrefixAndSuffix(words[i], words[j]))

        return count
