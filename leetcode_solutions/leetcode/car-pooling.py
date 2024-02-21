class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda x:x[2])
        size=trips[-1][2]
        print(size)
        arr=[0]*(size+1)
        for cap, s , e in trips:
            arr[s]+=cap
            arr[e]-=cap
        pref=[0]
        for i in range(size):
            pref.append(pref[-1]+arr[i])

        if max(pref)>capacity:
            return False
        else:
            return True 

        # [1 1 0 0]
        # [[2,1,5],[3,3,7]]