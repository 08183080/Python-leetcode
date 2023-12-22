from typing import List

def dfs(grid: List[List[str]], r: int, c: int):
    rows = len(grid)
    cols = len(grid[0])        
    if not (0 <= r < rows and 0 <= c < cols):
        return
    if grid[r][c] == 0:
        return
    if grid[r][c] != 1:
        return
    dfs(grid, r, c - 1)
    dfs(grid, r, c + 1)
    dfs(grid, r - 1, c)
    dfs(grid, r, c + 1)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        海洋上, 有几座岛屿呢...
        """
        rows = len(grid)
        cols = len(grid[0])