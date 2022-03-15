
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        
        if n == 1:
            return intervals
        sorted_list = sorted(intervals, key=itemgetter(0))
        idx = 0
        ans = []
        while idx < n:
            tmp = sorted_list[idx]
            
            if idx < n-1 and sorted_list[idx][1] < sorted_list[idx+1][0]:
                ans.append(tmp)
            elif idx < n-1 and sorted_list[idx][1] >= sorted_list[idx+1][0]:
                sorted_list[idx+1] = [sorted_list[idx][0], max(sorted_list[idx+1][1], sorted_list[idx][1])]
            else:
                ans.append(tmp)
            
            idx += 1
        
        return ans
