class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows=[set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")]
        return list(filter(lambda word: any(set(word.lower()) <= row for row in rows ),words))

        