from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1   # 湊出 0 元的方法只有一種

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
                print(f'coin: {coin}, i: {i}, dp: {dp}')
        return dp[amount]


s = Solution()
coins = [1,2,5]
amount = 5
ans = s.change(amount,coins)
print(ans)

'''
coin=1, i=1
dp[1] += dp[0]
dp = [1, 1, 0, 0, 0, 0]

coin=1, i=2
dp[2] += dp[1]
dp = [1, 1, 1, 0, 0, 0]

coin=1, i=3
dp[3] += dp[2]
dp = [1, 1, 1, 1, 0, 0]

coin=1, i=3
dp[4] += dp[3]
dp = [1, 1, 1, 1, 1, 0]

coin=1, i=4
dp[5] += dp[4]
dp = [1, 1, 1, 1, 1, 1]

coin=2, i=2
dp[2] += dp[0]
dp = [1, 1, 2, 1, 1, 1]

coin=2, i=3
dp[3] += dp[1]
dp = [1, 1, 2, 2, 1, 1]

coin=2, i=4
dp[4] += dp[2]
dp = [1, 1, 2, 2, 3, 1]

coin=2, i=5
dp[5] += dp[3]
dp = [1, 1, 2, 2, 3, 3]

coin=5, i=5
dp[5] += dp[0]
dp = [1, 1, 2, 2, 3, 4]

'''