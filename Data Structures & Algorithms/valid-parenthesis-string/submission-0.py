class Solution:
    def checkValidString(self, s: str) -> bool:
        # leftMin：最少有幾個左括號 '(' 還沒被配對
        # leftMax：最多有幾個左括號 '(' 還沒被配對
        leftmin, leftmax = 0, 0
        for c in s:
            if c == '(':
                leftmin += 1
                leftmax += 1
            elif c == ')':
                leftmin -= 1
                leftmax -= 1
            else:
                # 如果把 '*' 當成 ')' → 未配對左括號 -1
                # 如果把 '*' 當成 '(' → 未配對左括號 +1
                leftmin -= 1
                leftmax += 1
            # 把前面的 '*' 全部當成 '('，還是沒有足夠的左括號可以配對目前的 ')'
            if leftmax < 0:
                return False
            if leftmin < 0:
                leftmin = 0
        # 至少存在一種 '*' 的選法
        return leftmin == 0
