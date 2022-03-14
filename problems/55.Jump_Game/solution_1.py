class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) == 1:
            return True
        
        n = len(nums)
        destination = n - 1
        coverage = nums[0]
        idx = 0
        
        while idx < n:
            coverage = max(coverage, idx + nums[idx])
            
            if idx == coverage:
                if coverage >= destination:
                    return True
                return False
        
            idx += 1
        
        return True
