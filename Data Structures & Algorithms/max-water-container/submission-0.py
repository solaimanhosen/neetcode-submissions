class Solution:
    def computeArea(self, heights: List[int], l: int, r: int) -> int:
        return min(heights[l], heights[r]) * (r - l)

    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        maxi = 0
        while l <= r:
            maxi = max(maxi, self.computeArea(heights, l, r))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxi
