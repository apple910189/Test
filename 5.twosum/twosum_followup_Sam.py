from typing import List
class Solution:
    def twoSumAllPairs(self, nums:List[int], target: int):
        hashmap = {}
        ans = []
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                ans.append([hashmap[diff], i]) 
            else:
                hashmap[num] = i
        return ans
        

s = Solution()
nums = [1,2,1,2]
target = 3
ans = s.twoSumAllPairs(nums,target)
print(ans)