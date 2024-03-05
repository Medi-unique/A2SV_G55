class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        check={
            '2' : 'abc', '3': 'def' , '4' :'ghi' , '5' : 'jkl' , '6':'mno' , '7':'pqrs','8':'tuv','9':'wxyz'

        }
        result=[]
        path=[]
        n=len(digits)

        def helper(i):
            

            if len(path)==n  :
                result.append(''.join(path[:]))
                return 

            if len(path) > n:
                return 


            for j in check[digits[i]]:
                
                # curr=check[digits[i]]
                path.append(j)
                helper(i+1)
                path.pop()

        helper(0)
        print(result)
        return result if len(result) > 1 else []
