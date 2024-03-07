class Solution:
    def mySqrt(self, x: int) -> int:
        s=0
        e=x//2
        if  x==1:
            return 1
        while s <= e:
            mid =(s+e)//2
            if (mid*mid==x):
                return mid
            elif (mid*mid < x):
                s=mid+1
            else:
                e=mid-1
        return e




           