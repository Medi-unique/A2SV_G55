class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        s=len(nums)
        nums.sort(reverse=True)
        for i in range(1,s-1):
            if nums[i]+nums[i+1] > nums[i-1]:
                return sum(nums[i-1:i+2])
        return 0   
        
