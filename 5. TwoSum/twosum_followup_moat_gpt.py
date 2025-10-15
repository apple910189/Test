from typing import List
from collections import defaultdict

class Solution:
    def twoIntegerSumTarget(self, nums: List[int], target: int) -> List[List[int]]:
        hashMap = defaultdict(list)
        ans = []

        for i, num in enumerate(nums):
            diff = target - num
            if hashMap[diff]:  # 只要 list 有元素就能安全 pop
                j = hashMap[diff].pop()
                ans.append([j, i])
            else:
                hashMap[num].append(i)
        return ans


s = Solution()
nums = [1, 2, 2, 7]
target = 9
print(s.twoIntegerSumTarget(nums, target))  # [[0, 3], [1, 2]]
