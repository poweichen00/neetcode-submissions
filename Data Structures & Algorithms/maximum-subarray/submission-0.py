class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        cur = 0
        for n in nums:
            # 如果前面累積的總和已經是負數，重新從 0 開始
            if cur < 0:
                cur = 0
            cur += n
            maxsub = max(maxsub, cur)
        return maxsub