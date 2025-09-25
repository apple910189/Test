from collections import Counter


class Solution:
   def lengthOfLongestSubstring(self, s: str) -> int:
		left = 0
		seen = set()
		ans = 0

		for right in range(len(s)):
			while s[right] in seen:
				seen.remove(s[left])
				left += 1
			seen.add(s[right])
			ans = max(ans, right - left + 1)

		return ans

sol = Solution()
res = sol.lengthOfLongestSubstring('abcabcbb')
print(res)
