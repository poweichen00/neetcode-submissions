class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        # 排序規則：count[x] 越小越前面
        # 如果次數一樣，x 越大越前面
        nums.sort(key = lambda x : (count[x], -x))
        return nums