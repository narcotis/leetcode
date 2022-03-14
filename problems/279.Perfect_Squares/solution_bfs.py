class Solution:
    def numSquares(self, n) -> int:
        # n이 1 일경우
        # 1 ** 2 로 끝
        if n < 2:
            return 1
        
        # check list set init
        check_list = {n}
        
        # square list init
        square_list = [x**2 for x in range(1, int(n**0.5)+1)]
        
        cnt = 0
        
        while check_list:
            cnt += 1

            tmp_list = set()
            for val in check_list:
                for square in square_list:
                    if val == square:
                        return cnt

                    if val - square < 0:
                        break
                    
                    tmp_list.add(val - square)

                check_list = tmp_list
