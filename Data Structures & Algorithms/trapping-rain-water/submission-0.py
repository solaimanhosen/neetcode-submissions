class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)

        prefix_max = [0] * n
        prefix_max[0] = heights[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], heights[i])

        suffix_max = [0] * n
        suffix_max[-1] = heights[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], heights[i])

        water_area = 0
        for i, height in enumerate(heights):
            water_area += min(prefix_max[i], suffix_max[i]) - height

        return water_area
