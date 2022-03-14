def longestPalindrome(self, s: str) -> str:
        for i in reversed(range(len(s))):
            if s == s[::-1]:
                return s
            
        size = 1
        start = 0
        for i in range(1, len(s)):
            if i - size >= 0 and s[i-size:i+1] == s[i-size:i+1][::-1]:
                # size >= 0 인 이유는, 오른쪽 1개만 같은지 비교할것이기 때문.
                start = i - size
                size += 1
                # i - size 부터 i + 1 까지를 비교했기 때문에
                # start 는 i - size
            elif i - size >= 1 and s[i-size-1:i+1] == s[i-size-1:i+1][::-1]:
                start = i - size - 1
                size += 2
                # i - size - 1 부터 i + 1 까지를 비교했기 때문에
                # start는 i - size - 1 부터
            
        
        return s[start:start+size]
