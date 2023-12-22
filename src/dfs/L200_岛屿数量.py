from typing import List

def dfs(grid: List[List[str]], r: int, c: int):
    rows = len(grid)
    cols = len(grid[0])
    if not(0 <= r < rows and 0 <= c < cols):
        return
    if grid[r][c] == "0":
        return
    grid[r][c] = "0"
    dfs(grid, r - 1, c)
    dfs(grid, r + 1, c)
    dfs(grid, r, c - 1)
    dfs(grid, r, c + 1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        海洋上, 有几座岛屿呢...
        填海造陆, 神州陆沉...
        总有一些比记忆更重要的东西...
        """
        rows = len(grid)
        cols = len(grid[0])
        island_num = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_num += 1
                    dfs(grid, r, c)
        return island_num

s = Solution()
grid = grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(s.numIslands(grid))