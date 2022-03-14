def longestPalindrome(self, s: str) -> str:
        for i in reversed(range(len(s))):
            # len = 5 / i = 4
            # 0, 1, 2, 3, 4
            # [0:5] j : j + i + 1
            # 0, 1, 2, 3 / 1, 2, 3, 4
            # [0:4], [1:5]
            for j in range(len(s) - i):
                tmp = s[j:j+i+1]
                if tmp == tmp[::-1]:
                    return tmp
