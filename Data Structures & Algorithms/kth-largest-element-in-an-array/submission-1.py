class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-s for s in nums]
        heapq.heapify(nums)
        while k > 0:
            ans = heapq.heappop(nums)
            k -= 1
        return -ans