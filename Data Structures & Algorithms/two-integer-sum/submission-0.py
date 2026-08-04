class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            result = target - num
            if result in hash:
                return [hash[result], i]
            hash[num] = i
        return []