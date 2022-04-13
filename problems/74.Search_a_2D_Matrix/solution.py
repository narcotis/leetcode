class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = 0
        
        for i in range(len(matrix)):
            if target == matrix[i][0]:
                return True
            elif target < matrix[i][0]:
                i -= 1
                break
        
        for j in range(len(matrix[0])):
            if target == matrix[i][j]:
                return True
            else:
                j += 1
        
        return False
