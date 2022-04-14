import collections
import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic_t = collections.Counter(t)
        dic_s = {}
        
        tmp = set()
        
        res_size = sys.maxsize
        j = 0
        for i, c in enumerate(s):
            if c in dic_s:
                dic_s[c] += 1
            else:
                dic_s[c] = 1
            
            if c in dic_t and dic_t[c] <= dic_s[c]:
                tmp.add(c)
                while len(tmp) == len(dic_t):
                    # if t is in tmp
                    # then make the window size smaller
                    dic_s[s[j]] -= 1
                    
                    # after shortening the window,
                    # if window no longer contains t
                    if s[j] in dic_t and dic_t[s[j]] > dic_s[s[j]]:
                        # remove char from tmp_set
                        tmp.remove(s[j])
                        
                        # save the start, end, size of the window
                        if res_size > i-j+1:
                            start = j
                            end = i
                            res_size = i-j+1
                            
                    j += 1
        
        if res_size == sys.maxsize:
            return ""
        
        return s[start:end+1]
