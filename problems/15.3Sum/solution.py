class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) < 3:
            return ans

        nums.sort()
        
        for idx in range(len(nums)-2):
            i = idx + 1
            j = len(nums) - 1
        
            val = 0 - nums[idx]
            
            while i < j:
                if nums[i] + nums[j] == val:
                    tmp = [nums[idx], nums[i], nums[j]]
                    if tmp in ans:
                        pass
                    else:
                        ans.append([nums[idx], nums[i], nums[j]])
                    j -= 1
                elif nums[i] + nums[j] > val:
                    j -= 1
                else:
                    i += 1
            
            
        return ans
                
