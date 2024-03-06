class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]
        n=len(candidates)
        tar=target

        def helper(i,tar):
            if tar==0:
                result.append(path[::])
                return
            for j in range(i,n):
                if tar < 0:
                        return 
            
                path.append(candidates[j])
                helper(j,tar-candidates[j])
                path.pop()

        helper(0,tar)

        return result
        