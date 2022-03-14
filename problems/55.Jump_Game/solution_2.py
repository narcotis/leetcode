class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) == 1:
            return True
        
        destination = len(nums) - 1
        coverage = nums[0]
        idx = 0
        
        while idx <= coverage:
            coverage = max(coverage, idx + nums[idx])
            
            if coverage >= destination:
                return True
            
            idx += 1
        
        return False
