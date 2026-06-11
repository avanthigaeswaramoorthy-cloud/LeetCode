class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        d={}
        for i in range(len(pattern)):
            ch=pattern[i]
            word=words[i]
            if ch in d:
                if d[ch]!=word:
                    return False
            else:
                if word in d.values():
                    return False
            d[ch]=word
        return True
