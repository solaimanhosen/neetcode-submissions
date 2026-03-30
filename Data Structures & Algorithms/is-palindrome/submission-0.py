class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_s = re.sub(r"[^\w]", "", s).lower()

        return alnum_s == alnum_s[::-1]
