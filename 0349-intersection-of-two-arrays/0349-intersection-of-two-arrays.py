class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums1)
        res=[]
        s2=set(nums2)
        for nums in s1:
            if nums in s2:
                res.append(nums)
        return res