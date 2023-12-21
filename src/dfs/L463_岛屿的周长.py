from typing import List
"""
Ref: https://leetcode.cn/problems/island-perimeter/solutions/151724/tu-jie-jian-ji-er-qiao-miao-de-dfs-fang-fa-java-by/
"""

def dfs(grid: List[List[int]], r: int, c: int):
    row = len(grid)
    col = len(grid[0])
    if not (0 <= r < row and 0 <= c < col):
        return 1
    if grid[r][c] == 0:
        return 1
    if grid[r][c] != 1: # 标记已经走过的, 防止无限递归
        return 0
    grid[r][c] = 2
    return dfs(grid, r - 1, c) + dfs(grid, r + 1, c) + dfs(grid, r, c - 1) + dfs(grid, r, c + 1)      

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return dfs(grid, i, j)
   
s = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(s.islandPerimeter(grid))