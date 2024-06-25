from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        mx, my = min(r[0] for r in rectangles), min(r[1] for r in rectangles)
        ma, mb = max(r[2] for r in rectangles), max(r[3] for r in rectangles)
        lines = [(mx, my, mb, 'RIGHT'), (ma, my, mb, 'LEFT')]
        for x, y, a, b in rectangles:
            lines.append((x, y, b, 'LEFT'))
            lines.append((a, y, b, 'RIGHT'))
        lines.sort()

        index, low, high, side = 0, 0, 0, 'LEFT'
        for i, l, h, s in lines:
            if low == high:
                index, low, high, side = i, l, h, s
            elif side == s:
                if index != i or high != l:
                    return False
                high = h
            else:
                if index != i or low != l:
                    return False
                low, high = min(high, h), max(high, h)
                side = side if high > h else s
        return low == high


class Solution2:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corners = set()
        for x, y, a, b in rectangles:
            area += (a - x) * (b - y)
            corners ^= {(x, y), (x, b), (a, y), (a, b)}
        mx, my = min(r[0] for r in rectangles), min(r[1] for r in rectangles)
        ma, mb = max(r[2] for r in rectangles), max(r[3] for r in rectangles)
        return area == (ma - mx) * (mb - my) and corners == {(mx, my), (mx, mb), (ma, my), (ma, mb)}
