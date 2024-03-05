class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        path=[]
        
        def helper(i):
            if len(path) == k:
                result.append(path[:])
            if len(path) > k:
                return 
                
            for j in range(i+1,n+1):
                path.append(j)
                helper(j)
                path.pop()




        helper(0)
        return result
        