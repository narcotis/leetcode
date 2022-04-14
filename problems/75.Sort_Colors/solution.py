class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
        c = 0
        
        for num in nums:
            if num == 0:
                a += 1
            elif num == 1:
                b += 1
            else:
                c += 1
        
        nums[:a] = [0] * a
        nums[a:a+b] = [1] * b
        nums[a+b:a+b+c] = [2] * c


