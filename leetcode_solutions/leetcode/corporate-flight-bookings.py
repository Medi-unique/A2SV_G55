class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res=[0]*(n+1)
        for reserve in bookings:
            first,last,seat=map(int,reserve)
            res[first-1]+=seat
            res[last]-=seat
        pref=[res[0]]
        for i in range(1,len(res)):
            pref.append(pref[i-1]+res[i])
        pref.pop()
        return pref

            
        