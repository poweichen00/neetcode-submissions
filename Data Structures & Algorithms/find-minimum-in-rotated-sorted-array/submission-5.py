class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            # 情況 A：左半邊 [l, m] 是「有序遞增」的
            # [4, 5, 6, 1, 2]，l 指向 4，m 指向 6。4 <= 6 成立。
            # 左半邊是有序的，最小值絕對不可能藏在左半邊。
            if nums[l] <= nums[m]:
                l = m + 1
            # 情況 B：左半邊 [l, m] 是「無序」的（代表旋轉點在左半邊）
            # [6, 1, 2, 3, 4]，l 指向 6，m 指向 2。6 <= 2 不成立。
            # 這代表最小值一定落在 [l, m] 這個區間內。
            else:
                r = m - 1
        return res
