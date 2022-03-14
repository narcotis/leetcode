class Solution:
    def reverse(self, x: int) -> int:
        
        if x >= 0:
            maximum = 2 ** 31 - 1
            tmp = str(x)
            ans = int(tmp[::-1])
            if ans > maximum:
                return 0
            else:
                return ans
        else:
            minimum = 2 ** 31 * -1
            tmp = str(x)[1:]
            ans = int(tmp[::-1]) * -1
            if ans < minimum:
                return 0
            else:
                return ans
        
        
