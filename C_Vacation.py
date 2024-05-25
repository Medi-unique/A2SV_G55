import sys

input = lambda: sys.stdin.readline().strip()

listinput = lambda: list(map(int, sys.stdin.readline().strip().split()))



def solve():
    s=int(input())
    check=[]
    for i in range(s):
        happy = listinput()
        check.append(happy)
    # print(check)

    dp=check[0]
    n = 3
    for j in range(1,s):
        cur=check[j]
        new=[0]*n

        
        new[0]=cur[0]+max(dp[1],dp[2])
    
        new[1]=cur[1]+max(dp[0],dp[2])
    
        new[2]=cur[2]+max(dp[0],dp[1])
        dp=new
    print(max(dp))
    

s=1
# s = int(input())

for _ in range(s):
    solve()
