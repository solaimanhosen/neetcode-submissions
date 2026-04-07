class Solution:
    def trap(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        left_max, right_max = 0, 0
        water_area = 0
        while left < right:
            if heights[left] < heights[right]:
                left_max = max(left_max, heights[left])
                water_area += left_max - heights[left]
                left += 1

            else:
                right_max = max(right_max, heights[right])
                water_area += right_max - heights[right]
                right -= 1

        return water_area
