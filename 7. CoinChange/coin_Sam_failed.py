class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        count = 0
        for i, coin in enumerate(coins):
            while amount >= coin:
                amount -= coin
                count += 1
        if amount != 0:
            return -1
        return count