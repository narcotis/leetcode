class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text
        # text가 존재하며, pattern의 처음과 일치하거나 "." 인지 아닌지
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        
        # pattern이 2개 이상 존재하며, 다음 pattern이 "*" 일 경우
        if len(pattern) >= 2 and pattern[1] == '*':
            # "*"로 인해 2개 이후에도 일치하는지 혹은 현재 일치하는지
            # 2개 이후에도 일치하지 않고, 현재도 일치하지 않으면 False 가 먼저 나오기 때문에 다음으로 진행 X
            # 현재도 일치하고, 2개 이후에도 일치하면 다음으로 진행
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        # first_match 하며, 다음 i, idx를 재귀 호출
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
