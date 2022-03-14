class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        # jump cnt
        cnt = 0
        
        n = len(nums)
        destination = n - 1
        
        # maximum jump length
        coverage = 0
        last_idx = 0
        
        for i in range(n):
            coverage = max(coverage, i + nums[i])
            
            # no more idx to search
            if i == last_idx:
                # update cnt (jump)
                cnt += 1
                last_idx = coverage
            
                if coverage >= destination:
                    return cnt
