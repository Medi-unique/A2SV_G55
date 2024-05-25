import sys

input = lambda: sys.stdin.readline().strip()

listinput = lambda: list(map(int, sys.stdin.readline().strip().split()))



def solve():
    n = int(input())
    arr = listinput()
    dp=[0]*(n)
    dp[0]=0
    dp[1]=abs(arr[0]-arr[1])
    for i in range(2,n):
         dp[i] = min(dp[i - 1] + abs(arr[i] - arr[i - 1]), dp[i - 2] + abs(arr[i] - arr[i - 2]))
    print(dp[-1])
        
        
    
    

s=1
# s = int(input())
for _ in range(s):
    solve()