class Solution:
    def totalMoney(self, n: int) -> int:
        ans=0
        mondays=1
        for i in range(1,n//7 + 1):
            ans += sum(range(i,i+7))
            mondays +=1
        ans += sum(range(mondays,n%7 + mondays))
        return ans
        