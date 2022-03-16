class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        big_num = m + n - 2
        small_num = min(m,n) - 1
        
        
        mult = 1
        div = 1
        for i in range(small_num):
            mult *= (big_num - i)
            div *= (small_num - i)
            
        
        return int(mult / div)
