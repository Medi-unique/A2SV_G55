class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        s=len(nums)
        nums.sort()
        count=0
        


        for k in range(2,s):
            i,j=0,k-1
            while i < j:
                if nums[i]+nums[j]>nums[k]:
                    count+=j-i
                    j-=1
                else:
                    i+=1
            
            
        return count
        