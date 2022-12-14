from collections import deque


class Solution:

    def allPathsSourceTargetBfs(self,
                                graph: list[list[int]]) -> list[list[int]]:
        """
        Time Complexity: O(2^V * V)
            Graph with V verticies mean 2^(V-1) - 1 possible paths from start to end
            O(V) time to build each path
            (2^V-1 - 1) * O(V) = O(2^V * V)
        Space Complecity: O(2^V * V)
            queue contains at most O(2^V) paths
            each path will take O(V) space
        """
        paths = []
        if not graph or len(graph) == 0:
            return paths

        queue = deque()
        path = [0]
        queue.append(path)

        while queue:
            current_path = queue.popleft()
            node = current_path[-1]
            for next_node in graph[node]:
                temp_path = current_path.copy()
                temp_path.append(next_node)

                if next_node == len(graph) - 1:
                    paths.append(temp_path)
                else:
                    queue.append(temp_path)
        return paths

    def allPathsSourceTargetDfs(self,
                                graph: list[list[int]]) -> list[list[int]]:
        """
        Time Complexity: O(2^V * V)
            DAG can have 2^V-1 - 1 possible paths
            O(V) time to build each path
        Space Complexity: O(V)
            Recursion depth can be no more than V
        Process:
            add cur to path
            if node is end of graph add current path to paths
            else cycle thru list of degrees and search
            then remove self from current path if none match
        """
        paths = []
        path = []

        def dfs(node):
            path.append(node)
            if node == len(graph) - 1:
                paths.append(path.copy())
                return

            next_nodes = graph[node]
            for next_node in next_nodes:
                dfs(next_node)
                path.pop()

        if not graph or len(graph) == 0:
            return paths
        dfs(0)
        return paths


graph = [[1, 2], [3], [3], []]
expected = [[0, 1, 3], [0, 2, 3]]
s = Solution()
actual = s.allPathsSourceTarget(graph)
print(f'expected={expected}.\nactual={actual}')
