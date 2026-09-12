class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        # 目前候選起點
        start = 0
        # 從 start 出發目前剩下的油
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            # 如果油量變成負數，目前 start 不可能成功
            if tank < 0:
                # 下一站重新當起點
                start = i + 1
                tank = 0
        return start