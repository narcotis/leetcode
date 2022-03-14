class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ""
        cnt = 0
        
        for char in s:
            if char in ans:
                ans = ans[ans.index(char)+1:]
                ans += char
            else:
                ans += char
                if cnt <= len(ans):
                    cnt = len(ans)
            print(ans, cnt)
        
        return cnt
        
