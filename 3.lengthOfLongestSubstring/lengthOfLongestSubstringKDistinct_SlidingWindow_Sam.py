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

'''
利用right往右移動，每一次移動，都判斷當前對應的字符是否在字典裡，如果不在，就新增到字典，如果已經存在，就把對應的value加一。 
在加入字典之前，要先判斷字典的長度，如果小於等於K，才能加入字典，如果大於K，要做兩件事。
第一，字典中對應到當前left位置的字符value減一
第二，left加一。 不斷重複這個動作，直到字典長度小於等於K
'''

