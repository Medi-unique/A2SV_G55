class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        check=nums[0]

        if nums[0]< nums[r]:
            return nums[0]

        while l < r:
            mid=(l+r)//2

            if nums[mid] >= check:
                
                 l=mid+1


            else:
                r=mid

            
        return nums[l]
        

   