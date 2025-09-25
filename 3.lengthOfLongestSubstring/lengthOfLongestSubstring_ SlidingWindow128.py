class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		left = 0
		right = 0
		cnt = [0] * 128  # ASCII table size
		ans = 0

		while right < len(s):
			print(f'r:{right} l:{left}')
			while cnt[ord(s[right])] > 0:
				# 如果s right>0 表示有重複，要讓left指到重複的地方，減一
				cnt[ord(s[left])] -= 1
				print(f' del {ord(s[left])}')
				printCnt(cnt)
				left += 1
				window = s[left:right]
				print(f"<刪> left={left}, right={right}, window='{window}', ans={ans}")
			cnt[ord(s[right])] += 1
			print(f' add {ord(s[right])}')
			printCnt(cnt)
			ans = max(ans, right - left + 1)
			right += 1
			window = s[left:right]
			print(f"<增> left={left}, right={right}, window='{window}', ans={ans}")
			print()

		return ans

def printCnt(cnt):
	print('[', end='')
	for i,v in enumerate(cnt):
		if v:
			print(f'{i} ', end='')
	print(']')

sol = Solution()
res = sol.lengthOfLongestSubstring('abcdde')
print(res)


