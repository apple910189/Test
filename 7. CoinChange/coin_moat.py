from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1 for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                if i >= j and dp[i - j] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i - j] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[amount]


s = Solution()
coins = [2]
amount = 6
ans = s.coinChange(coins,amount)
print(ans)