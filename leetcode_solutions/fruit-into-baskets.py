class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        l=0
        maxi=0
        check=Counter()
        for r in range(n):
            check[fruits[r]]+=1
            while len(check)>2:
                  check[fruits[l]]-=1
                  if check[fruits[l]]==0:
                      check.pop(fruits[l])
                  l+=1
           
            maxi=max(r-l+1,maxi)
        return maxi

        