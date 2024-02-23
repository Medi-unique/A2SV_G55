class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for l in s:
            if l=='(':
                stack.append(0)
            else:
                prev=stack.pop()
                stack[-1] += max(1,prev*2)
        return stack[-1]
        