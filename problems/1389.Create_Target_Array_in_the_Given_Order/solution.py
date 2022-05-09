class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        tmp = []
        
        for i in range(len(nums)):
            tmp.insert(index[i], nums[i])
        
        return tmp
