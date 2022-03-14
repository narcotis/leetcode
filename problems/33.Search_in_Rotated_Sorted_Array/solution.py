class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx1 = nums[0]
        idx2 = nums[-1]
        
        if target >= idx1:
            for i in range(len(nums)):
                if target == nums[i]:
                    return i
                
                if i+1 < len(nums) and nums[i] > nums[i+1]:
                    return -1
        else:
            if target > idx2:
                return -1
            
            for i in reversed(range(len(nums))):
                if target == nums[i]:
                    return i
                
                if i-1 > 0 and nums[i] < nums[i-1]:
                    return -1
            
        return -1
