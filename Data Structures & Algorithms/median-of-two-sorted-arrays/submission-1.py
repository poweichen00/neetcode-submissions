class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        # half 代表「合併後陣列的左半邊」應該有的元素總數
        # 例如總數為 4，half = 2 (左邊 2 個，右邊 2 個)
        # 例如總數為 5，half = 2 (左邊 2 個，右邊 3 個，中位數在右邊第一個)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            # i 是陣列 A 的分割點索引。代表 A 的左半邊包含索引 0 到 i 共 i + 1 個元素
            i = (l + r) // 2
            # j 是陣列 B 的分割點索引。
            # 因為陣列索引從 0 開始，所以 B 的分割點索引 j = (half - (i + 1)) - 1 = half - i - 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # A 的左半邊太大了，代表分割點 i 太靠右，必須往左移
                r = i - 1
            else:
                # B 的左半邊太大了，代表分割點 i 太靠左，必須往右移
                l = i + 1
