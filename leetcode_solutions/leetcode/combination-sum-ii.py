class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]
        n=len(candidates)
        candidates.sort()
        tar=target

        def helper(i,tar):
            p=-20
            if tar==0:
                result.append(path[::])
                return
            for j in range(i,n):
                if tar < 0:
                        return 
                if candidates[j] == p:
                    continue
            
                path.append(candidates[j])
                helper(j+1,tar-candidates[j])
                p=path.pop()

        helper(0,tar)

        return result
        