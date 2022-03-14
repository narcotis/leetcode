class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        square = 0
        
        i = 0
        j = len(height) -1

        while i < j:
            min_height = min(height[i], height[j])
            tmp_square = (j-i) * min_height
            
            square = max(square, tmp_square)
            
            # 두 높이를 비교해서, 작은쪽을 이동
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        
        return square
