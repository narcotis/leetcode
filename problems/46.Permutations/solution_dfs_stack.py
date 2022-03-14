class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        if len(nums) == 1:
            return [nums]
        
        results = []
        prev_elements = []
    
        def dfs(elements) :
            if len(elements) == 0 :
                results.append(prev_elements[:])

            for e in elements :
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results
