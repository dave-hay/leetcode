class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        the char determines final index
        """
        last_index = {char: i for i, char in enumerate(s)}
        start = end = 0
        partitions = []

        for i, char in enumerate(s):
            end = max(end, last_index[char])
            if i == end:
                partitions.append(i - start + 1)
                start = i + 1
        return partitions
