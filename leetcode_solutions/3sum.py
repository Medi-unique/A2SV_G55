# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res=[]
#         for i,n in enumerate(nums):
#             if i>0 and n==nums[i-1]:
#                 continue
#             j,k=i+1,len(nums)-1
#             while j<k:
               
#                   threesum=n+nums[i]+nums[j]
#                   if threesum > 0 :
#                       k-=1
#                   elif threesum < 0:
#                       j+=1
#                   else :
#                       res.append([n,nums[j],nums[k]])
#                       print(res)
#                       j+=1
#                       while nums[j]==nums[j-1] and j<k:
#                              j+=1
#         return    res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for  i,n in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l < r:
                threesum=n+nums[l]+nums[r]
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l+=1
                else :
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res


