from typing import List

class Solution:
    def numberOfWayCoinsChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1;
        for j in coins:
            for i in range(amount + 1):
                if i >= j:
                    dp[i] += dp[i - j]; 
        return dp[amount]


s = Solution()
coins = [1,2,5]
amount = 5
ans = s.numberOfWayCoinsChange(coins,amount)
print(ans)