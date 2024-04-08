class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Time O(n): arrays equal size; iter thru each once
        Space O(1): map only has 2 keys
        """
        freqs = {0: 0, 1: 0}

        for st in students:
            freqs[st] += 1

        for sandwich in sandwiches:
            if freqs[sandwich] > 0:
                freqs[sandwich] -= 1
            else:
                return sum(freqs.values())

        return 0
