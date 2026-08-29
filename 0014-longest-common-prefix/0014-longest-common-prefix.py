class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=strs[0]
        for x in strs:
            while not x.startswith(ans):
                ans=ans[:-1]
        return ans