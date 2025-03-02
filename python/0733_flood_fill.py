from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """
        recursive
        keep going until all origional colors filled
        bfs
        """
        ROWS, COLS = len(image), len(image[0])
        og = image[sr][sc]
        seen = set()
        q = deque([(sr, sc)])

        while q:
            r, c = q.popleft()

            if (
                (r, c) in seen
                or r not in range(ROWS)
                or c not in range(COLS)
                or image[r][c] != og
            ):
                continue

            image[r][c] = color

            seen.add((r, c))

            for xr, xc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                q.append((r + xr, c + xc))

        return image
