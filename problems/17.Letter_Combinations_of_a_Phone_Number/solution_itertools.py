import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        # alphabets per digit init
        alpha_dict = {}
        alpha_dict["2"] = ["a","b","c"]
        alpha_dict["3"] = ["d", "e", "f"]
        alpha_dict["4"] = ["g", "h", "i"]
        alpha_dict["5"] = ["j","k","l"]
        alpha_dict["6"] = ["m","n","o"]
        alpha_dict["7"] = ["p","q","r","s"]
        alpha_dict["8"] = ["t","u","v"]
        alpha_dict["9"] = ["w","x","y","z"]
        
        # 각 digit별 values들을 list로 묶음
        tmp = [alpha_dict[x] for x in digits]
        
				# list로 묶여진 digit들을 product
        ans = list(itertools.product(*tmp))
        
				# product결과 tuple로 나오기 때문에, join으로 묶어줌
        for i in range(len(ans)):
            ans[i] = "".join(ans[i])
            
        return ans
