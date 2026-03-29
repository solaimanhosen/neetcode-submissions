class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return []
