class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        my_nums={}
        for key,value in enumerate(nums):
            my_nums[value]=key

        for i,k in operations:
            nums[my_nums[i]]=k
            my_nums[k]=my_nums.pop(i)

        return nums