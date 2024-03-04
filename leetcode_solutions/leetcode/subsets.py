class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=[]
        temp=[]

        def backtrack(i):
            result.append(temp[:])
            if i == n:
                return 

            for j in range(i,n):

                temp.append(nums[j])
                print(temp)
                backtrack(j+1)
                temp.pop()


        backtrack(0)
        return result
    

        