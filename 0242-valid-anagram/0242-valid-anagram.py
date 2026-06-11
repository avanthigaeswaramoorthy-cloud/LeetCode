class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s)!=len(t):
          return False
       d={}
       for ch in s:
          d[ch]=d.get(ch,0)+1
       for ch in t:
          if ch not in d:
            return False
          d[ch]-=1
          if d[ch]<0:
            return False
       return True

                