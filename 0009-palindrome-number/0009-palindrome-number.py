class Solution:
    def isPalindrome(self, x: int) -> bool:
        res=str(x)
        rev=""
        if x==0:
            return True
        while x>0:
            dig=x%10
            rev=rev+str(dig)
            x=x//10
        if rev==res:
            return True
        else:
            return False