from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                return [i, hashMap[target-nums[i]]]
            hashMap[nums[i]] = i
        raise Exception("can not find two integer whose sum is targe")


s = Solution()
nums = [1,2]
target = 7
ans = s.twoSum(nums,target)
print(ans)