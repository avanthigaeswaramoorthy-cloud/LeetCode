class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        c=0
        for x in nums[:]:
            if x==0:
                c+=1
                nums.remove(x)
        while c>0:
            nums.append(0)
            c-=1
        return nums
