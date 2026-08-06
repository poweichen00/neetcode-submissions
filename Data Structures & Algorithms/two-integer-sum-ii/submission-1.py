class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l <= r:
            ans = numbers[l] + numbers[r]
            if ans > target:
                r -= 1
            elif ans < target:
                l += 1
            elif ans == target:
                return [l+1, r+1]
        return 