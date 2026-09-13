class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for t in triplets:
            # 一旦某個位置超過 target，就不可能再變小回來
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3