class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        n = len(s)
        pairs = {')':'(',']':'[','}':'{'}
        for c in s:
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                else:
                    a = stack.pop()
                    continue
            stack.append(c)
        return not stack

s = Solution()
text = "{()"
ans = s.isValid(text)
print(ans)