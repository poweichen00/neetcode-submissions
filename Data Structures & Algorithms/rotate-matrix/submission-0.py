class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            # r - l 這一邊需要處理幾個元素
            for i in range(r - l):
                top, bot = l, r
                # 左上角目前的值暫存起來
                topleft = matrix[top][l + i]
                # 左下 -> 左上
                matrix[top][l + i] = matrix[bot - i][l]
                # 右下 -> 左下
                matrix[bot - i][l] = matrix[bot][r - i]
                # 右上 -> 右下
                matrix[bot][r - i] = matrix[top + i][r]
                # 原本左上 -> 右上
                matrix[top + i][r] = topleft
            l += 1
            r -= 1


