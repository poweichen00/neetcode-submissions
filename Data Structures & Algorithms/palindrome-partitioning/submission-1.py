class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def back(i, cur):
            if i >= len(s):
                res.append(cur.copy())
                return
            for j in range(i, len(s)):
                if self.ispali(s, i, j):
                    cur.append(s[i:j+1])
                    back(j+1, cur)
                    cur.pop()
        back(0, [])
        return res
    def ispali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True