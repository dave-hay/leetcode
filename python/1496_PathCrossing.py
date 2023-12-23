class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = {(0, 0)}
        dirs = {"N": 1, "S": -1, "E": 1, "W": -1}
        x = 0
        y = 0

        for d in path:
            if d in "NS":
                y += dirs[d]
            else:
                x += dirs[d]

            if (x, y) in seen:
                return True
            seen.add((x, y))

        return False
