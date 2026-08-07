class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        for i in range(1, len(nums)):
           output[i] = output[i-1] * nums[i-1]
        right = 1
        for i in range(n-1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output