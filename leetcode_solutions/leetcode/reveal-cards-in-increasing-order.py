class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n=len(deck)
        index=deque(range(n))
        answer=[0]*n
        deck.sort()
        for val in deck:
            first=index.popleft()
            answer[first]=val
            if index:
                index.append(index.popleft())
        return answer


        