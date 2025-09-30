from typing import List
class Solution:
    def twoSumAllPairs(self, nums:List[int], target: int):
        hashmap = {}
        ans = []
        used = set()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap and hashmap[diff] not in used:
                used.add(hashmap[diff])
                used.add(i)
                ans.append([hashmap[diff], i]) 
            else:
                hashmap[num] = i
            print(hashmap)
        return ans
        

s = Solution()
nums = [1,2,2,7]
target = 9
ans = s.twoSumAllPairs(nums,target)
print(ans)