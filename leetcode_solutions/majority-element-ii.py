class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        val=len(nums)//3
        output=[]
        for i in nums:
            if nums.count(i)>val:
                output.append(i)
        return set(output)
            