class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt = 0
        i = 0
        tmp = 0
        while i < len(arr):
            tmp = max(tmp, arr[i])

            if tmp == i:
                cnt += 1
            
            i += 1

        return cnt
