from typing import List
class Solution:
    def twoSum(self, nums:List[int], target: int):
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            else:
                hashmap[num] = i
        print('can not find any pairs of answer')

s = Solution()
nums = [1,2]
target = 7
ans = s.twoSum(nums,target)
print(ans)