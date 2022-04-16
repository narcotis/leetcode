import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        for i in range(len(nums)+1):
            for seq in itertools.combinations(nums, i):
                ans.append(seq)
        
        return ans
