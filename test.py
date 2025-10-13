from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -999
        for i in range(len(nums)):
            for j in range(len(nums)):
                currSum =0
                if j == i:
                    currSum = nums[i]
                    maxSum = max(maxSum,currSum)
                else:
                    for a in range(i,j+1):
                        currSum = currSum + nums[a]
                        print(f'{i} {j} {nums[a]}')
                        maxSum = max(maxSum,currSum)
        return maxSum

nums = [5,4,-1,7,8]
s = Solution()
ans = s.maxSubArray(nums)
print(ans)