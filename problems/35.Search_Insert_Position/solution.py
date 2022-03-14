class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # worst cases
        if target > nums[-1]:
            return len(nums)
        
        if target < nums[0]:
            return 0
        
        low = abs(target - nums[0])
        high = abs(target - nums[-1])
        
        if low <= high:
            for i in range(len(nums)):
                if nums[i] >= target:
                    return i                
        else:
            for i in reversed(range(len(nums))):
                if nums[i] == target:
                    return i
                
                if target > nums[i]:
                    return i+1

