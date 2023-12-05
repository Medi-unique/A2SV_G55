class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ""
        
        i = 0
        while i < len(num) - 2:
            if num[i] == num[i + 1] == num[i + 2]:
                current = num[i:i + 3]
                if current > largest:
                    largest = current
                i += 3
            else:
                i += 1
        
        return largest