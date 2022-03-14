class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        maximum = 0
        for values in accounts:
            tmp = sum(values)
            if tmp >= maximum:
                maximum = tmp
        
        return maximum
