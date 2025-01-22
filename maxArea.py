class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        result = 0

        while p1 < p2:
            shorter = min(heights[p1], heights[p2])
            area = (p2 - p1) * shorter
            #(p2 - p1) * whichever p1 or p2 height is shorter
            if area > result:
                result = area #set result to new area if it is larger
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return result