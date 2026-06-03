class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in range(len(nums)):
            n=nums[i]
            if n in d:
                return True
            d[n]=i
        return False
            