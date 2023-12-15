from typing import List

def dfs(graph: List[List[int]], num: int, n: int, path: List[int]):
    if (num == n - 1):  # 终止条件 
        path.append(num)
        print(path)
        return
    # path.append(num)
    for i in graph[num]:
        path.append(i)
        dfs(graph, i, n, path)
        path.remove(i)


class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        path = list()
        dfs(graph, 0, n, path)

s = Solution()
graph = [[1,2],[3],[3],[]]
s.allPathsSourceTarget(graph)