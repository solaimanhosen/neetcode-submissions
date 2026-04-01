class Solution:
    def twoSum(self, nums: List[int], target: int, i) -> List[int]:
        j, k = i + 1, len(nums) - 1

        res = []
        while j < k:
            total = nums[j] + nums[k]
            if total > target:
                k -= 1
            elif total < target:
                j += 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        result = []
        i = 0
        for i, num in enumerate(nums):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            res = self.twoSum(nums, -nums[i], i)
            if len(res):
                result.extend(res)

        return result
