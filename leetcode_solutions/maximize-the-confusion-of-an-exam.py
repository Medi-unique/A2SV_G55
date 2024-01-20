from collections import Counter

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        l = 0
        max_consecutive = 0
        max_count = 0
        window = Counter()

        for r in range(n):
            window[answerKey[r]] += 1
            max_count = max(max_count, window[answerKey[r]])

            if (r - l + 1) - max_count > k:
                window[answerKey[l]] -= 1
                l += 1

            max_consecutive = max(max_consecutive, r - l + 1)

        return max_consecutive
