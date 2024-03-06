class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # l,r=0,len(nums)-1
        res=[-1,-1]

        # while l<=r:
        #     mid=(l+r)//2

        #     if nums[mid] > target:
        #         r=mid-1
        #     elif nums[mid] < target:
        #         l=mid+1
        #     else:
        #         if nums[l]==target:
        #             res[0]=l
        #             l+=1
        #         # if nums[r]==target:
        #         #     res[1]=r
        #         #     r-=1
        if target in nums:
            res[0]=bisect_left(nums,target)
            res[1]=bisect_right(nums,target)-1
                
        return res
        