class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for num in range(32):
            # 二進位的 1 左移 i 位，再跟 n 做 AND 
            if (1 << num) & n:
                res += 1
        return res