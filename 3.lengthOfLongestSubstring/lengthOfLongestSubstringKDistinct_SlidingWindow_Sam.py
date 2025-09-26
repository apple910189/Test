class Solution:
	def longestSubstringWithAtMostKDistinctCharacters(self, s: str, k:int) -> int:
		left = 0
		right = 0
		# cnt = [0] * 128  # ASCII table size
		ans = 0
		cnt = {}

		while right < len(s):
			if s[right] in cnt:
				cnt[(s[right])] += 1
			else:
				cnt[(s[right])] = 1
			while len(cnt) > k:
				cnt[(s[left])] -= 1
				if cnt[(s[left])] == 0:
					del cnt[(s[left])]
				left +=1
			ans = max(ans, right - left + 1)
			right += 1
		return ans

def printCnt(cnt):
	print('[', end='')
	for i,v in enumerate(cnt):
		if v:
			print(f'{i} ', end='')
	print(']')

sol = Solution()
ans = sol.longestSubstringWithAtMostKDistinctCharacters('abaccc',2)
print(f'ans:{ans}')


