class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # 先把 n 放進 res，只會跑 0 ~ n-1，不會包含 n
        res = n
        for i in range(n):
            # 相同的數字最後會互相抵消，剩下的就是缺少的那個數字
            res ^= i ^ nums[i]
        return res
