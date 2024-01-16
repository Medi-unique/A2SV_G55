class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix=[]*len(nums)
        curr=0
        for num in nums:
            curr+=num
            prefix.append(curr)
        return prefix