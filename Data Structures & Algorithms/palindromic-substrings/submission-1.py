class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            # 奇數
            res += self.pali(s, i, i)
            # 偶數
            res += self.pali(s, i, i + 1)
        return res
    def pali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res 

