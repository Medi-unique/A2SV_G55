class Solution:
    def isHappy(self, n: int) -> bool:
        encountered = set()

        while n != 1:
            n = sum(int(digit) ** 2 for digit in str(n))

            if n in encountered:
                return False

            encountered.add(n)

        return True