class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        
        ans = set()
        for i in range(len(nums)):
            tmp = ""
            cnt = 0
            for j in range(i, len(nums)):
                if nums[j] % p == 0:
                    cnt += 1
                
                if cnt > k:
                    break
                
                tmp += str(nums[j]) + ","
                ans.add(tmp)
        
        return len(ans)
