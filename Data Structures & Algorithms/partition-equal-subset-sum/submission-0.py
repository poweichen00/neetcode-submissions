class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        # 目前可以組合出哪些總和
        dp = set()
        # 一開始什麼數字都不選，可以組成的總和就是 0
        dp.add(0)
        target = sum(nums) // 2
        for i in range(len(nums)-1, -1, -1):
            # 加入 nums[i] 之後，所有可能形成的新總和
            nextdp = set()
            for t in dp:
                nextdp.add(t+nums[i])
                # 不選 nums[i]，原本的總和 t 還是保留下來
                nextdp.add(t)
            dp = nextdp
        return True if target in dp else False
