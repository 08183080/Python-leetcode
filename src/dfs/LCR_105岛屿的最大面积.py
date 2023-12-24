import math
from typing import List

def dfs(grid: List[List[int]], x: int, y: int) -> int:
    cnt = 0
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
        return 0
    if grid[x][y] == 0:
        return 0
    grid[x][y] = 0
    cnt += 1
    # print(cnt)
    return cnt + dfs(grid, x + 1, y) + dfs(grid, x - 1, y) + dfs(grid, x, y - 1) + dfs(grid, x, y + 1)
    

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(grid, i, j))
        return ans     

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
s = Solution()
print(s.maxAreaOfIsland(grid))