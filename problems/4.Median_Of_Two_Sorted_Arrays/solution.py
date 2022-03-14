class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums = nums1 + nums2
        nums.sort()
        
        med = len(nums) // 2
        if len(nums) % 2 == 0:
            ans = (nums[med-1] + nums[med]) / 2
        else:
            ans = nums[med]
        
        return ans
