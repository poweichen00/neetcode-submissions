class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 假設最大乘積就是 nums[0]
        res = nums[0]
        # curmax：到目前位置為止，連續子陣列的最大乘積
        # curmin：到目前位置為止，連續子陣列的最小乘積
        # curmin， 負數 × 負數，可能變成很大的正數
        curmin, curmax = 1, 1
        # 1. num * 舊 curmax → 把目前數字接在之前最大乘積後面
        #
        # 2. num * 舊 curmin → 如果 num 是負數，負數 × 最小負數可能變最大正數
         #
        # 3. num → 不接前面，直接從目前這個 num 重新開始
        for num in nums:
            tmp = num * curmax
            curmax = max(num * curmax, num * curmin, num)
            curmin = min(tmp, num * curmin, num)
            res = max(res, curmax)
        return res

