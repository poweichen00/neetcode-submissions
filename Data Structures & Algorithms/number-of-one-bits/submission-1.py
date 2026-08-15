class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for num in range(32):
            if (1 << num) & n:
                res += 1
        return res