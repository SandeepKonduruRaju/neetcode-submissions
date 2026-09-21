class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        maxwater = 0
        r = len(heights) - 1
        while l < r:
            maxwater = max(maxwater,(r-l)*min(heights[l],heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxwater