class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path=[]
        result=[]
        n=len(nums)

        def helper(i):
            if len(path)==n:
                result.append(path[::])
                
            
            for j in range(i,n):
                if nums[j] not in path:
                    path.append(nums[j])
                    helper(i)
                    path.pop()
            return
        helper(0)
        return result

        
        