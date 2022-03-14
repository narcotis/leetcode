class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [False] * n
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                continue
            else:
                dp[nums[i]-1] = True
        
        for i in range(n):
            if dp[i]:
                continue
            else:
                return i+1
        
        return n+1
