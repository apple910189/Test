class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # charToNextIndex stores the index after current character
        charToNextIndex = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in charToNextIndex:
                i = max(charToNextIndex[s[j]], i)

            ans = max(ans, j - i + 1)
            charToNextIndex[s[j]] = j + 1
            print(f's:{s[j]} j:{j} i:{i} ans:{ans} map:{charToNextIndex}')
        return ans

sol = Solution()
res = sol.lengthOfLongestSubstring('pwwkew')
print(res)

'''
一個n，大小為s的長度
一個ans=0
一個map={}
for總共計算n次，每一次是j

    每一次for，判斷一個字母是否在map裡，
        如果在map裡，判斷字母在map的index，跟i比對
    將字母加入map，他的index為j+1
    ans在for裡計算，能進入for就至少ans=1，ans用j-i+1計算

'abcabcbb'
n=8
j=0,
i=0map{a=1},ans=1


'bbbbb'
'pwwkew'



'''
