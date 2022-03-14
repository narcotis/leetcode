class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alpha_dict = {}
        alpha_dict["2"] = "abc"
        alpha_dict["3"] = "def"
        alpha_dict["4"] = "ghi"
        alpha_dict["5"] = "jkl"
        alpha_dict["6"] = "mno"
        alpha_dict["7"] = "pqrs"
        alpha_dict["8"] = "tuv"
        alpha_dict["9"] = "wxyz"
        
        if len(digits) == 0:
            return []
        
        
        ans = list(alpha_dict[digits[0]])
        
        if len(digits) == 1:
            return ans
        
        for i in range(1, len(digits)):
            tmp = []
            for val in ans:
                for char in alpha_dict[digits[i]]:
                    tmp.append(val + char)
            ans = tmp
        
        return ans
