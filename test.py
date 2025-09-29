class Solution(object):
    def isValid(self, s):
        stack = []
        openBrackets = '([{'
        closeBrackets = '}])'
        for c in s:
            if c in openBrackets:
                stack.append(c)
            else:
                for i in range(3):
                    if c == closeBrackets[i]:
                        if len(stack) != 0 and stack[-1] == openBrackets[i]:
                            stack.pop()
                        else:
                            return False
        if len(stack) == 0:
            return True
        else:
            return False
s = Solution()
text = "{()"
ans = s.isValid(text)
print(ans)