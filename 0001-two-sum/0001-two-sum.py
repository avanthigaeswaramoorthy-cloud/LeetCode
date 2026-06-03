class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            com=target-nums[i]
            if com in d:
                return (d[com],i)
            d[nums[i]]=i