from typing import List

class Solution(object):
    def dfs(self, x: int, parent: int, e:List[List[List[int]]]) -> int:
        res = 0
        for edge in e[x]:
            if edge[0] == parent:
                continue
            res += edge[1] + self.dfs(edge[0], x, e)
        return res


    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        e = [[] for _ in range(n)]
        for edge in connections:
            e[edge[0]].append([edge[1], 1])
            e[edge[1]].append([edge[0], 0])
        return self.dfs(0, -1, e)