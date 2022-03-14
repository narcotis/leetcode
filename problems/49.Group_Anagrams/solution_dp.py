class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # 상하반전 후 x, y 교체
        x = len(matrix)
        y = len(matrix[0])
        
        print(x//2)
        # 상하반전 먼저
        for i in range(x//2):
            matrix[i], matrix[x-1-i] = matrix[x-1-i], matrix[i]
                
        # x, y 반전
        for i in range(x):
            for j in range(y):
                if i > j:
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
