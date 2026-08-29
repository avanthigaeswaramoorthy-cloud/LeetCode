class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k=s.split()
        k=k[-1]
        t=len(k)
        return t