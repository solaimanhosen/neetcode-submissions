class Solution:
    def isValid(self, s: str) -> bool:
        isMatch = {
            ')': '(', 
            '}': '{',
            ']': '['
        }

        st = []
        for ch in s:
            if ch in isMatch.values():
                st.append(ch)
            elif not st or st[-1] != isMatch[ch]:
                return False
            else:
                st.pop()

        return len(st) == 0
