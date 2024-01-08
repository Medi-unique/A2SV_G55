class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        limit=len(piles)//3
        large=0
        for i in range((len(piles)-2),limit-1,-2):
            large+=piles[i]
        return large

        