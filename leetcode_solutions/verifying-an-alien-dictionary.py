class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        new = sorted(words, key=lambda word: [order.index(c) for c in word])
        if new == words:
            return True
        