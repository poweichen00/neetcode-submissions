class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            # 如果最遠可以跳到的位置 >= res
            if i + nums[i] >= res:
                # 只要想辦法跳到 i 就可以了，把新的目標位置改成 i
                res = i
        return res == 0