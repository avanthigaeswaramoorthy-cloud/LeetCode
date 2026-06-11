class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for ch in magazine:
            d[ch]=d.get(ch,0)+1
        for ch in ransomNote:
            if ch not in d:
                return False
            d[ch]-=1
            if d[ch]<0:
                return False
        return True
           