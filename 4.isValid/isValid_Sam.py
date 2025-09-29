class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        n = len(s)
        map_parantheses = {')':'(',']':'[','}':'{'}
        # map_parantheses = {'(':')','[':']','{':'}'}
        pop_array = [')',']','}']
        for c in s:
            print(f'start {c}')
            if c in pop_array:
                if len(stack)==0 or stack[-1] != map_parantheses[c]:
                    print('stack=0 or not match')
                    return False
                else:
                    a = stack.pop()
                    print(f'pop:{a}')
                    continue
            print(f'add:{c}')
            stack.append(c)
        if len(stack)==0:
            return True
        else:
            return False

s = Solution()
text = "{()}"
ans = s.isValid(text)
print(ans)