import re
class Solution:
    def myAtoi(self, s: str) -> int:
        
        compiler = re.compile('[0-9]+')
    
        ans = ""
        plus = True
        found = False
        for i in range(len(s)):
            if s[i] == ' ':
                if found:
                    break
                continue
            elif s[i] == '-':
                if found:
                    break
                plus = False
                if i+1 < len(s) and compiler.match(s[i+1]):
                    continue
                else:
                    return 0
            elif s[i] == '+':
                if found:
                    break
                plus = True
                if i+1 < len(s) and compiler.match(s[i+1]):
                    continue
                else:
                    return 0
            elif compiler.match(s[i]):
                found = True
                ans += s[i]
            else:
                break
        
        if ans == "":
            return 0
        elif plus:
            if int(ans) > 2 ** 31 -1:
                return 2 ** 31 -1
            else:
                return int(ans)
        else:
            if int(ans) * -1 < 2 ** 31 * -1:
                return 2 ** 31 * -1
            else:
                return int(ans) * -1
                
