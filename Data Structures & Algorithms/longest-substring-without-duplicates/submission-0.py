class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        sub_len = 0

        qu = deque()
        for ch in s:
            counter[ch] += 1
            qu.append(ch)
            while counter[ch] > 1:
                counter[qu.popleft()] -= 1

            sub_len = max(sub_len, len(qu))

        return sub_len