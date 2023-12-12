class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def list_sum(arr, lvl):
            total = 0

            for nl in arr:
                if nl.isInteger():
                    total += nl.getInteger() * lvl
                else:
                    total += list_sum(nl.getList(), lvl + 1)
            return total

        return list_sum(nestedList, 1)
