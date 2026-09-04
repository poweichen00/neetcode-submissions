class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # 最後會得到：cnt = {'a': 3, 'b': 3, 'c': 3}
        cnt = defaultdict(int)
        # 一個字串一個字串看
        for w in words:
            # 再把字串裡的每個字母拿出來
            for c in w:
                cnt[c] += 1
        for c in cnt:
            # 如果這個字母的總數，不能被字串數量整除，代表沒辦法平均分給每個字串
            if cnt[c] % len(words):
                return False
        return True