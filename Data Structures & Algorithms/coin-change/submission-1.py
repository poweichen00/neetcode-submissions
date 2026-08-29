class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # memo[5] = 2，代表湊出 5 最少需要 2 枚硬幣
        memo = {}
        def dfs(amount):
            # base case：如果剩餘金額剛好是 0
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            # 設一個非常大的數字
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    # 1 代表「現在用了這一枚 coin」
                    # dfs(amount - coin)，代表剩下的金額最少還需要幾枚硬幣
                    res = min(res, 1 + dfs(amount - coin))
            # 記住 amount 的答案
            memo[amount] = res
            return res
        mincoin = dfs(amount)
        return -1 if mincoin >= 1e9 else mincoin