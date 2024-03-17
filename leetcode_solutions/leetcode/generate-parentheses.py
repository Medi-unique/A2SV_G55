class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generateCombinations(n, current, rem_closing):
            if n == 0:
                while rem_closing:
                    current += ')'
                    rem_closing -= 1
                return [current]
            else:
                if rem_closing:
                    return generateCombinations(n-1, current+'(', rem_closing+1) + generateCombinations(n, current+')', rem_closing-1)
                else:
                    return generateCombinations(n-1, current+'(', rem_closing+1)
        return generateCombinations(n, '', 0)