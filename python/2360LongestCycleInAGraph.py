class Solution:
    def __init__(self):
        self.answer = -1

    def dfs(self, node, edges, dist, visit):
        visit[node] = True
        neighbor = edges[node]

        if neighbor != -1 and not visit[neighbor]:
            dist[neighbor] = dist[node] + 1
            self.dfs(neighbor, edges, dist, visit)
        elif neighbor != -1 and neighbor in dist:
            self.answer = max(self.answer, dist[node] - dist[neighbor] + 1)

    def longestCycle(self, edges: List[int]) -> int:
        length = len(edges)
        visit = [False for _ in range(length)]

        for i in range(length):
            if visit[i]:
                continue
            dist = {i: 1}
            self.dfs(i, edges, dist, visit)

        return self.answer
