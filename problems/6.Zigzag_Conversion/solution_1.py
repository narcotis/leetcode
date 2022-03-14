class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # ((numRows-1)-i) * 2

        if numRows == 1:
            return s        
        
        ans = ""
        for i in range((numRows)):
            if i % (numRows-1) == 0:
                j = i
                while j < len(s):
                    ans += s[j]
                    j += (numRows-1) * 2
            else:
                j = i
                while j < len(s):
                    ans += s[j]
                    if j + ((numRows-1)-i)*2 < len(s):
                        ans += s[j + ((numRows-1)-i)*2]
                    j += (numRows-1) * 2 
        
        return ans
