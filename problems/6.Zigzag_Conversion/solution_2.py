class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # ((numRows-1)-i) * 2

        if numRows == 1:
            return s        
        
        ans_list = [""] * numRows
        pos = 0
        way = 1
        for i, letter in enumerate(s):
            ans_list[pos] += letter
            pos += way
        
            if pos % (numRows -1) == 0:
                way *= -1
        
        return "".join(ans_list)
            
        

