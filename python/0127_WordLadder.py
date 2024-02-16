from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        adj list
        bfs to endWord
        """

        wordList.append(beginWord)
        pre2Word = defaultdict(list)
        word2Pre = defaultdict(list)

        # each empty ch type

        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1 :]
                word2Pre[word].append(key)
                pre2Word[key].append(word)

        q = deque([beginWord])
        seen = set(beginWord)
        count = 1

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == endWord:
                    return count

                for pre in word2Pre[cur]:
                    for word in pre2Word[pre]:

                        if word in seen:
                            continue

                        seen.add(word)
                        q.append(word)

            count += 1

        return 0
