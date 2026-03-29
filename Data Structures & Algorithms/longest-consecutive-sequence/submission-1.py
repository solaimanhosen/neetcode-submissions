class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def get_count(n):
            if n not in seen:
                count[n] = 0
            else:
                count[n] = 1 + get_count(n - 1)

            return count[n]

        seen = set(nums)
        count = defaultdict(int)
        max_len = 0
        for num in nums:
            if num - 1 not in count:
                count[num  - 1] = get_count(num - 1)
            count[num] = count[num - 1] + 1
            max_len = max(max_len, count[num])

        return max_len
