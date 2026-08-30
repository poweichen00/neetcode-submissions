class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 多開一格是為了表示「字串結尾」
        dp = [False] * (len(s)+1)
        # 如果已經走到字串最後面，代表前面的單字都成功匹配完成
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                # 1. i + len(w) 不能超過字串範圍
                # 2. 從 s[i] 開始，長度 len(w) 的字串，是否剛好等於 w
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    # 如果目前這個單字 w 可以匹配，那 dp[i] 是否為 True
                    # 就要看「匹配完 w 之後剩下的字串」
                    dp[i] = dp[i+ len(w)]
                if dp[i]:
                    break
        return dp[0]
