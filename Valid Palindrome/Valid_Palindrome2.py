class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lst = []
        for word in s:
            if word.isalnum():
                lst.append(word)
        return lst == lst[::-1]