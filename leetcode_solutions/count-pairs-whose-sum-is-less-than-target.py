class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i,j,l,count=0,1,len(nums),0
        """  [-1,1,1,2,3], target = 2

             [-1,-2,-6,-7,2,3,5], target = -2
              
        
        
         """
        nums.sort()
        for i in range(l):
            for j in range(i+1,l):
                if nums[i]+nums[j]<target:
                    count+=1    
        return count
        
            
