class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        common_strings = {}
        min_index_sum = float('inf')
        
        for i, n in enumerate(list1):
            if n in list2:
                j = list2.index(n)
                index_sum = i + j
                
                if index_sum < min_index_sum:
                    result = [n]
                    min_index_sum = index_sum
                elif index_sum == min_index_sum:
                    result.append(n)
        
        return result