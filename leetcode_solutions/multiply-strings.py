class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                product = digit1 * digit2

                pos1 = i + j
                pos2 = i + j + 1
                sum_ = product + result[pos2]

                result[pos1] += sum_ // 10
                result[pos2] = sum_ % 10

        start = 0
        while start < len(result) and result[start] == 0:
            start += 1

        return "".join(map(str, result[start:]))