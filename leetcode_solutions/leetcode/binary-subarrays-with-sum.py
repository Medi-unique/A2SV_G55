class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        curSum = 0
        hashmap = {}
        count = 0
        for i in range(len(nums)):
            
            if curSum in hashmap:
                hashmap[curSum] +=1
            else:
                hashmap[curSum] = 1
            curSum += nums[i]      

            if (curSum - goal) in hashmap: 
                count += hashmap[curSum - goal] 
        return count