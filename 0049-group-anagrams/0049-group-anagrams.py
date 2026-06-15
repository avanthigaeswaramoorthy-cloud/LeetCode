
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       hash_map=defaultdict(list)
       for s in strs:
          freq=[0]*26
          for ch in s:
            freq[ord(ch)-ord('a')]+=1
          key=tuple(freq) 
          hash_map[key].append(s)
       return list(hash_map.values())
