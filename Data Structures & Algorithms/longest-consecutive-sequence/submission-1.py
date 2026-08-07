class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxcount = 0
        for i in nums:
            if i - 1 not in nums:
                current = i
                count = 1
                while current + 1 in nums:
                    current += 1
                    count += 1
                maxcount = max(maxcount, count)
        return maxcount
