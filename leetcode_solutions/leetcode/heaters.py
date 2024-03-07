class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n = len(houses)
        houses.sort()
        heaters.sort()

        ans = 0

        for house in houses:
            if house in heaters:
                continue
            else:
                temp = bisect_left(heaters, house)
                if temp >= len(heaters):
                    ans = max(ans, abs(heaters[-1]-house))
                elif temp == 0:
                    ans = max(ans, heaters[0]-house)
                else:
                    ans = max(ans, min(house-heaters[temp-1], heaters[temp]-house))
         
        return ans

        
        