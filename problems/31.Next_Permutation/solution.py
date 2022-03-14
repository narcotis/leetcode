class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # worst case
        sort_nums = sorted(nums)
        sort_nums.reverse()
        if sort_nums == nums:
            nums.sort()
            return
        
        # init
        idx = 0
        i = 0
        j = len(nums) - 1
        
        # Check last i:N[i] < N[i+1]
        while idx+1 < len(nums):
            if nums[idx] < nums[idx+1]:
                i = idx
            idx += 1
            
        # Find last j:N[j] > N[i]
        while j > 0:
            if nums[j] > nums[i]:
                break
            j -= 1
        
        # Swap N[i] and N[j]
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        
        nums[i+1:] = reversed(nums[i+1:])
        return
