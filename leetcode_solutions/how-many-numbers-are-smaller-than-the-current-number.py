class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
      sorted_nums=sorted(nums) 
      res=[] 
      for n in nums:
          res.append(sorted_nums.index(n))
      return res
        