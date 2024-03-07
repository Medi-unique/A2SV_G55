class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = 0
        r = sum(weights)

        def canShip (mid):
            count = 1
            remain = mid
            for weight in weights:
                if weight > mid:
                    return False
                remain -= weight
                if remain < 0:
                    count += 1
                    remain = mid- weight
            return count <= D

        
        while l < r:
            mid = (l + r) // 2
            if canShip(mid):
                r = mid
            else:
                l = mid + 1

        return l