class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def help(arr):
            if len(arr) == 1:
                return arr[0]

            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])

            return dp[-1] 
        return max(help(nums[1:]), help(nums[:-1]))

