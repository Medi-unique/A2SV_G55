class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix=[0]
        for num in nums:
            prefix.append(num+prefix[-1]) 
        for i,n in enumerate(nums):                       
            if prefix[-1]-prefix[i+1]==prefix[i+1]-n:
                return i
        return -1