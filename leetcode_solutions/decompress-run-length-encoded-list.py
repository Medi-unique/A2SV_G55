class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        #evens are repeated odds value times
        result=[]
        for i,n in enumerate(nums):
            if  i%2==0 and i+1 < len(nums):
                for j in range(n):
                    result.append(nums[i+1])
        return result
            