class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        tot,mindif=0,float('inf')
        diff=0
        res=0
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                tot=nums[i]+nums[l]+nums[r]
                if tot == target:
                    return tot
                elif tot < target:
                    l+=1
                else:
                    r-=1
                diff=abs(tot-target)
                if diff<mindif:
                    mindif=diff
                    res=tot
        return res
              
                

