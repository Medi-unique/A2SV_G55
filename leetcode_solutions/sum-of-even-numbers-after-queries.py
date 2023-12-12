
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even_sum = sum(x for x in nums if x % 2 == 0)

        for val, index in queries:
            original_val = nums[index]
            nums[index] += val

            if original_val % 2 == 0:
                even_sum -= original_val

            if nums[index] % 2 == 0:
                even_sum += nums[index]

            result.append(even_sum)

        return result
