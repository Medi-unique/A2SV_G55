class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
        
        if not strs:
            return prefix
        
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for j in range(1, len(strs)):
                currentStr = strs[j]
                if i >= len(currentStr) or currentStr[i] != ch:
                    return prefix
            prefix += ch
        
        return prefix