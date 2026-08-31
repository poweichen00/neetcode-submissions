class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS[i]：nums[i] 當作開頭時，從 i 往右可以組成的最長遞增子序列長度
        LIS = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    # 接上 nums[j]
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)