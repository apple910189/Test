class Solution(object):
    def isValid(self, s):
        stack = []
        openBrackets = "({["
        closeBrackets = ")}]";
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
text = "{]"
ans = s.isValid(text)
print(ans)

'''
建立stack
把每個字讀進來
開兩個string，一個紀錄開的，一個紀錄關的，順序一樣
如果是open，就push
如果是close，先檢查if stack[-1] == openBrackets[i]，不等於就return false
最後檢查stack長度，如果>0就return false else return true

test case:
""
'()'
'[]'
'{}'
'('
')'
'''