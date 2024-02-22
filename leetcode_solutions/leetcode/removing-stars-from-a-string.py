class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for l in s:
            if stack and l=='*':
                stack.pop()
            else:
                stack.append(l)
        return ''.join(map(str,stack))