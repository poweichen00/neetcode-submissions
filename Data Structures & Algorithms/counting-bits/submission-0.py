class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        # offset 代表目前最大的 2 的次方
        offset = 1
        for i in range(1, n+1):
            # 如果 i 剛好走到下一個 2 的次方
            # offset = 1，i = 2，更新 offset = 2
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp