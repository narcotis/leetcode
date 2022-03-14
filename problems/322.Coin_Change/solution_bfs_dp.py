class Solution(object):
    def coinChange(self, coins, amount) -> int:
        # 0 일 경우 그냥 0
        if amount == 0:
            return 0
        
        coins.sort()
        check_list = {amount}
        # caching을 위해 init
        visited = [False]* (amount+1)
        
        cnt = 0
        visited[-1] = True
        while check_list:
            cnt += 1
            
            tmp_list = set()
            
            for val in check_list:
                for coin in coins:
                    tmp = val - coin
                    if tmp == 0:
                        return cnt
                    
                    if tmp < 0:
                        break
                    elif not visited[tmp]:
                        visited[tmp] = True
                        tmp_list.add(tmp)
                        
            if len(tmp_list) == 0:
                return -1
            else:
                check_list = tmp_list
        
        
                        
