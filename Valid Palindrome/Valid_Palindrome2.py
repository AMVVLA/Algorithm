class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lst = []
        for word in s:
            if word.isalnum():
                lst.append(word)
        if lst == lst[::-1]:
            return 1
        else:
            return 0