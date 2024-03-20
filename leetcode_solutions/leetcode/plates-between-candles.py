class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        check=[]
        result=[]
        n=len(s)
        for i in range(n):
            if s[i]=='|':
                check.append(i)
        print(check)


        for l,r in queries:
            cl=bisect_left(check,l)
            cr=bisect_right(check,r)-1

            ans=0
            if cr>cl:
                ans=(check[cr]-check[cl])-(cr-cl)
            
            print(ans)
            result.append(ans)
        return result
        

        