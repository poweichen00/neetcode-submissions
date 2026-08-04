class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        res = [0] * 26
        for char in s:
            res[ord(char) - ord('a')] += 1
        for char in t:
            res[ord(char) - ord('a')] -= 1
        return all(v == 0 for v in res)
            
