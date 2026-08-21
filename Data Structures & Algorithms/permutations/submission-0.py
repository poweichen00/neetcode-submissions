class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []

        def backtrack():
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return

            for n in nums:
                if n in permutation:
                    continue
                permutation.append(n)
                backtrack()
                permutation.pop()

        backtrack()
        return res