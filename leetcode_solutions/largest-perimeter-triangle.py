class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
         #         for 3 numbers to make a triangle the sum of any two sides must be greater                       than the remaining side
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if  nums[i]<nums[i+1]+nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
            else:  i+=1
        return 0
            
        