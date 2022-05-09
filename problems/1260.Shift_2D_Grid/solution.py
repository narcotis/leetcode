class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        tmp = []
        
        m = len(grid)
        n = len(grid[0])
        
        if k % (m*n) == 0:
            return grid
        
        if m*n == 1:
            return grid
        
        for nums in grid:
            tmp += nums
        
        tmp = tmp[m*n-k%(m*n):] + tmp[:m*n-k%(m*n)]
        return [tmp[i:i+n] for i in range(0, m*n, n)]
        
        
