from collections import deque


class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        answer = [0] * len(temps)
        stack = []

        for i, t in enumerate(temps):
            while stack and t > stack[-1][0]:
                _, stackInd = stack.pop()
                answer[stackInd] = i - stackInd
            stack.append((t, i))

        return answer


class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        if len(temps) == 1:
            return [0]

        answer = deque()
        stack = []

        for i in range(len(temps) - 1, -1, -1):
            cur = temps[i]

            if stack and cur >= stack[-1][0]:
                while stack and cur >= stack[-1][0]:
                    stack.pop()

            if not stack:
                answer.appendleft(0)
            else:
                answer.appendleft(stack[-1][1] - i)

            stack.append([cur, i])

        return answer
