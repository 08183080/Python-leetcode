from typing import List

class Solution:
    def __init__(self):
        self.ans = []

    def dfs(self, graph: List[List[int]], num: int, n: int, path: List[int]):
        if (num == n - 1):  # 终止条件 
            self.ans.append(path[:])
            # print(path)
            return
        # path.append(num)
        for i in graph[num]:
            path.append(i)
            self.dfs(graph, i, n, path)
            path.pop()

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        path = list()
        path.append(0)
        self.dfs(graph, 0, n, path)
        print(self.ans)
        return self.ans

s = Solution()
graph = [[4,3,1],[3,2,4],[3],[4],[]]
s.allPathsSourceTarget(graph)