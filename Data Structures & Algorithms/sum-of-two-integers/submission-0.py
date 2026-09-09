class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 0xFFFFFFFF = 32 個 1 限制 Python 的整數只保留 32-bit
        mask = 0xFFFFFFFF
        # 0x7FFFFFFF = 2147483647 用來判斷結果是正數還是負數
        maxint = 0x7FFFFFFF
        while b != 0:
            # 找出哪些 bit 同時都是 1 這些位置做加法時會產生進位
            carry = (a & b) << 1
            # XOR 可以做到不考慮進位的加法 mask：限制結果在 32-bit 範圍內
            a = (a ^ b) & mask
            # 把剛剛算出的進位交給下一輪繼續把 a 和 carry 相加
            b = carry & mask
        # 如果 a > maxint：在 32-bit 中它其實是負數
        # ~(a ^ mask) 用來把 32-bit 補數形式 轉回 Python 的負整數
        return a if a <= maxint else ~(a ^ mask)
        