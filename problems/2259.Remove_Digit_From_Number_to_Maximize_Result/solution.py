class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        tmp = number.find(digit)
        
        ans = 0
        while tmp != -1:
            if tmp == -1:
                break        
            ans = max(ans, int(number[:tmp]+number[tmp+1:]))
            tmp = number.find(digit, tmp+1)
        
        return str(ans)
        
