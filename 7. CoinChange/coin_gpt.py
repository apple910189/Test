from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 建立 dp 陣列，長度為 amount + 1
        # dp[i] 表示湊出 i 元最少需要的硬幣數
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 湊出 0 元需要 0 枚硬幣
        # 主要的遞推過程
        for i in range(1, amount + 1):  # 從 1 到 amount
            for coin in coins:
                if i - coin >= 0:
                    # 這裡要寫遞推公式，更新 dp[i]
                    dp[i] = min(dp[i], dp[i - coin] + 1)
                    print(f"After computing amount {i}, dp = {dp[:i+1]}")

        # 若 dp[amount] 沒被更新過，表示無法湊出
        return dp[amount] if dp[amount] != float('inf') else -1


s = Solution()
coins = [1,2,5]
amount = 11
ans = s.coinChange(coins,amount)
print(ans)

'''
coins = [1, 3, 4]
amount = 6

我可以用最後一枚硬幣來完成它，那最後一枚硬幣可能是1、2或5。
f(11) = min(
    f(11 - 1) + 1,
    f(11 - 2) + 1,
    f(11 - 5) + 1
)

這意思是：
如果最後一枚是1，那前面要湊出 f(10)
如果最後一枚是2，那前面要湊出 f(9)
如果最後一枚是5，那前面要湊出 f(6)
然後再多加1枚硬幣（最後那一枚）。

重點想法：
用最少的硬幣湊出每個金額。
先求出所有「小金額」的最優解，再用它們去推「大金額」。
'''
