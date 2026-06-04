class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1={}
        dic2={}
        for i in range(len(s)):
            c1=s[i]
            c2=t[i]
            if c1 in dic1:
                if dic1[c1]!=c2: 
                    return False
            else:
                dic1[c1]=c2

            if c2 in dic2:
                if dic2[c2]!=c1:
                    return False
            else:
                dic2[c2]=c1
        return True