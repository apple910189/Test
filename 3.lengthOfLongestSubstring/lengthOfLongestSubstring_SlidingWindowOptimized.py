class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		n = len(s)
		ans = 0
		# charToNextIndex stores the index after current character
		charToNextIndex = {}

		i = 0
		# try to extend the range [i, j]
		for j in range(n):
			print(f'j:{j} s:{s[j]} i:{i} map:{charToNextIndex}')
			if s[j] in charToNextIndex:
				print(f' {s[j]} in map')
				i = max(charToNextIndex[s[j]], i)

			ans = max(ans, j - i + 1)
			charToNextIndex[s[j]] = j + 1

		return ans

sol = Solution()
res = sol.lengthOfLongestSubstring('abcabcbb')
print(res)

'''

'''