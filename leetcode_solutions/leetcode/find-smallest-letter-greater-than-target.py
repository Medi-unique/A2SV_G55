class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for l in letters:
            if target < l:
                return l
        return letters[0]
        