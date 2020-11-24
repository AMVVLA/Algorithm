class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        ans = ''
        def move(self, s, l, r):
            while l >= 0 and r <= len(s) and s[l] == s[r - 1]:
                l -= 1
                r += 1
            return s[l + 1:r - 1]
        for i in range(len(s) -1):
            ans = max(ans, move(self,s, i, i+1), move(self,s, i, i+2), key=len)
        return ans