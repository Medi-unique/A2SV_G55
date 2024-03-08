from bisect import bisect_left, bisect_right


s=int(input())
arr=list(map(int,input().split()))
arr.sort()
days=int(input())
for i in range(days):
    cur=int(input())
    print(bisect_right(arr,cur))
