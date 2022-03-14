class Solution(object):
    def isMatch(self, text, pattern):
        # 함수 안에 memo를 정의
        # 그 안에서 재귀 함수를 별도로 실행, memo를 통한 caching
        memo = {}
        def dp(i, j):
            print(memo)
            print(i, j)
            
            # memo없으면 (실행한적이 없으면)
            # (i,j) 째로 dict의 key가 됨
            if (i, j) not in memo:
                
                # pattern의 마지막 일 경우
                if j == len(pattern):
                    # text 끝까지 왔는지 비교
                    ans = i == len(text)
                else:
                    # first_match 하는지
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    
                    # 다음 pattern이 존재하고, "*"일 경우
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        # 다음 * 까지 제외하고 진행해도 first_match 하는지
                        # 혹은 현재 first_match 하는지
                        # 둘중 하나라도 맞아야 다음 text로 넘어감
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        # first_match 하면 다음 text, pattern 진행
                        ans = first_match and dp(i+1, j+1)
                # 진행 결과를 memo
                memo[i, j] = ans
                
            return memo[i, j]

        return dp(0, 0)
