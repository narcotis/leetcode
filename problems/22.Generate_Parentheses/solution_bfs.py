class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # res init
        res = [('', 0)]
        
        # 전체 길이 까지 다다를때 까지
        for i in range(n*2):
            sub_res = []
            # res 의 sequence와 num
            for seq, num in res:
                # ( 의 개수가 n: 기준치 보다 작을 경우
                # ( 를 추가하고, num ++
                if num < n:
                    sub_res.append((seq + '(', num + 1))
                
                # ( 의 개수가 총 길이 / 2 보다 클 경우 (?)
                # ) 추가 및 num 유지
                if num > len(seq)/2:
                    sub_res.append((seq + ')', num))
                print(sub_res)
            res = sub_res
        return [r[0] for r in res]
