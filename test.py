import collections

class Solution:
    def longestSubstringWithAtMostKDistinctCharacters(self, s: str, k:int) -> int:
        n = len(s)
        left = 0
        counter = collections.Counter()
        ans = 0
        for right in range(n):
            counter[s[right]] +=1
            while len(counter) > k:
                counter[s[left]] -=1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left +=1
            ans = max(ans, right - left + 1)
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


print(6.57/87.86)