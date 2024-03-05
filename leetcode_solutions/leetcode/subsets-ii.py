class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=[]
        path=[]
        nums.sort()
        resultset=set()

        def helper(i):
            if tuple(path) not in resultset:
                result.append(path[:])
                resultset.add(tuple(path))
            if len(path) > n:
                return 
            for j in range(i,n):
                # if nums[j] not in path:
                    path.append(nums[j])
                    helper(j+1)
                    path.pop()





        helper(0)
        return result
        