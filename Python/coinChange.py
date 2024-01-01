class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # result = self.minCoins(coins, amount, {})
        result = self.minCoinsTabulation(coins, amount)
        return result if result != math.inf else -1
    
    def minCoinsTabulation(self, coins, amount):
        dp = [math.inf for _ in range(amount + 1)]
        dp[0] = 0

        for amt in range(1, amount + 1):
            for coin in coins:
                if amt-coin >= 0:
                    dp[amt] = min(dp[amt], dp[amt-coin] + 1)
        return dp[amount]


    def minCoins(self, coins, amount, memoise):
        if amount in memoise:
            return memoise[amount]
        
        if amount == 0:
            return 0
        
        if amount <0:
            return math.inf
        
        minCoins = math.inf

        for coin in coins:
            minCoins = min(minCoins, self.minCoins(coins, amount-coin, memoise))
        
        memoise[amount] = minCoins+1
        return minCoins + 1