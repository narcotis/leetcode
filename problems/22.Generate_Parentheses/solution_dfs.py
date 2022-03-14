class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # result init
        result = []
        
        def search(s, i, j):
            if i > n or j > n or j > i:
                return
            
            if len(s) == n * 2:
                result.append(s)
                return
            
            
            search(s + "(", i + 1, j)
            search(s + ")", i, j + 1)
        
        search("(", 1, 0)
        return result
