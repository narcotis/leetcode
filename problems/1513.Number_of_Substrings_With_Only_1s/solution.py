class Solution:
    def numSub(self, s: str) -> int:
        
        i = 0
        tmp = 0
        cnt = 0
        while i < len(s):
            if s[i] == "1":
                tmp += 1
                cnt += tmp
            else:
                tmp = 0
            
            i += 1
        
        return cnt % (10**9 + 7)
