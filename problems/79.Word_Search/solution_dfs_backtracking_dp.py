class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        
        def dfs(idx, y, x):
            if x < 0 or y < 0 or x == m or y == n:
                return False
            
            if word[idx] == board[y][x]:
                if idx == len(word)-1:
                    return True
                
                cur = board[y][x]
                
                board[y][x] = "#"
                
                found = dfs(idx+1, y+1, x) or dfs(idx+1, y, x+1) or dfs(idx+1, y-1, x) or dfs(idx+1, y, x-1)
                
                board[y][x] = cur
                
                return found
        
        
        return any([dfs(0, y, x) for y in range(n) for x in range(m)])
