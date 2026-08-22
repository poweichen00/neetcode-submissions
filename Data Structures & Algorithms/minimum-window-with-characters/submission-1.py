class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        # count: 記錄字串 t 中每個字元「需要」的數量
        # window: 記錄目前滑動視窗中每個字元「實際」的數量
        count, window = {}, {}
        # 統計目標字串 t 的字元頻率
        for c in t:
            count[c] = 1 + count.get(c, 0)
        # need: 總共需要滿足幾種字元的條件 (count 字典的 key 數量)
        # have: 目前視窗中已經「達標」的字元種類數
        have, need = 0, len(count)
        res, reslen = [-1, -1], float('inf')
        l = 0
        # 右指針 r 向右移動
        for r in range(len(s)):
            # 取出右指針指向的字元
            c = s[r]
            window[c] = 1 + window.get(c, 0) 
            # 如果這個字元是 t 需要的，且視窗中的數量等於需要的數量   
            if c in count and count[c] == window[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < reslen:
                    res = [l, r]
                    reslen = (r - l + 1)
                # 踢出左指針指向的字元，嘗試縮小視窗
                window[s[l]] -= 1
                # 踢出的字元是 t 需要的，踢出後視窗中的數量小於需要的數量
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if reslen != float('inf') else ""

         