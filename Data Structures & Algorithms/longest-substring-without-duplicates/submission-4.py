class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftOf = {}
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in leftOf:
                left = max(left, leftOf[ch] + 1)
            max_len = max(max_len, right - left + 1)
            leftOf[ch] = right

        return max_len
