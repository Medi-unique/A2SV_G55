import sys

input = lambda: sys.stdin.readline().strip()

listinput = lambda: list(map(int, sys.stdin.readline().strip().split()))




def solve():
    n,k= listinput()
    arr = listinput()
    dp=[0,abs(arr[0]-arr[1])]

    for i in range(2,n):
        num,s,val=i,k,float('inf')
        while s>0 and num>0:
            num-=1
            s-=1
            val=min(val,abs(arr[i]-arr[num])+dp[num])
        dp.append(val)

    print(dp[-1])



s=1
# s = int(input())
for _ in range(s):
    solve()