class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def dfs(cur, cur_sum):
            if cur_sum == target:
                ans.append(cur)
                return
            
            if cur_sum > target:
                return
            
            for num in candidates:
                dfs(cur + [num], cur_sum + num)            
        
        dfs([], 0)
        
        
        return ans
