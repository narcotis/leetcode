class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dct = {"(": ")", "[": "]", "{": "}"}
	
        for c in s:
            if c in "([{":
                stack += dct[c]
            elif not stack or c != stack.pop():
                return False
        return not stack
