class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        res = 0
        while True:
            slow = nums[slow]
            res = nums[res]
            if slow == res:
                return res