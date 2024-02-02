import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums) 
        pref=[1]
        res=[]

        for i in  range(n):
            pref.append(pref[-1]*nums[i])


        check=nums.count(0)
       
        if check==0:

            res=[pref[-1]//nums[j-1] for j in range(1,n+1)]
           
        elif check==1:
            
            res=[0]*n
            ind=nums.index(0)
            nums[ind]=1
            val= math.prod(nums)
            res[ind]=val
        else:
            return [0]*n
        return res
        