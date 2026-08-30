class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=""
        for x in s:
            if x.isalnum():
                a+=x
        if a==a[::-1]:
            return True
        else:
            return False