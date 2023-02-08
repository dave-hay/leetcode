class Solution:
    """
    Greedy
    Time: O(n)
    Space: O(1)

    Create a goal post for which the index needs to reach
    Iterate from the last index
    if cur index can reach the goal then update the goal
    if goal == 0 then that means nums[0] can reach the end
    """

    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(goal, -1, -1):
            if nums[i] + i >= goal:
                goal = i

        return goal == 0


class Solution:
    """
    Dynamic Programming
    Time: O(n^2)
    Space: O(n)
    """

    def canJump(self, nums: List[int]) -> bool:
        res = [False] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            iVal = nums[i]
            if nums[i] + i >= len(nums) - 1:
                res[i] = True
                continue

            for options in res[i : i + iVal + 1]:
                if options:
                    res[i] = True
                    break

        return res[0]
