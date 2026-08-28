class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = 從 index i 開始，到字串結尾，總共有幾種 decode 方法
        # base case:
        # 如果已經走到字串最後面 len(s)，代表成功完成一種解碼方式
        dp = {len(s) : 1}
        def dfs(i):
            # 如果這個位置已經算過，從 dp 拿答案
            if i in dp:
                return dp[i]
            # '0' 不能自己單獨解碼，沒有 0 -> 字母 的對應
            if s[i] == '0':
                return 0
            # 先把目前這一個數字當成一個字母
            #
            # 例如："226"
            #  i
            # 先解 "2"，剩下從 index i+1 繼續
            res = dfs(i+1)
            # 嘗試把目前兩個數字一起解碼，合法範圍只能是 10 ~ 26
            # s[i] == '1' → 10 ~ 19 都合法
            # s[i] == '2' 且下一個字元在 0~6 → 20 ~ 26 合法
            if (i+1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in "0123456")):
                # 如果可以兩個數字一起解碼，就從 i+2 繼續算
                res += dfs(i+2)
            # 把 index i 的答案記起來
            dp[i] = res
            return res
        return dfs(0)
