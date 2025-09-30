from typing import List

class Solution:
    def twoIntegerSumTarget(self, nums: List[int], target: int) -> List[List[int]]:
        hashMap = {}
        ans = []
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                list = []
                targetList = hashMap.get(target - nums[i])
                print(targetList)
                list.append(targetList[-1])
                list.append(i)
                ans.append(list)
                targetList.pop()
                if len(targetList) == 0:
                    hashMap.pop(target - nums[i])
            else:
                if not nums[i] in hashMap:
                    hashMap[nums[i]] = []
                hashMap[nums[i]].append(i)
        return ans

s = Solution()
nums = [1,2,3,4,5,6,7]
target = 7
ans = s.twoIntegerSumTarget(nums,target)
print(ans)