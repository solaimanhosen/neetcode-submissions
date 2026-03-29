class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_right = [1 for _ in range(len(nums) + 1)]
        right_left = [1 for _ in range(len(nums) + 1)]

        for i, num in enumerate(nums):
            left_right[i + 1] = left_right[i] * nums[i]
            right_left[-1 - (i + 1)] = right_left[-1 - i] * nums[-1 - i]

        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            ans[i] = left_right[i] * right_left[i + 1]

        return ans
