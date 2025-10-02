from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[List[int]]:
        ans = []
        hashmap = defaultdict(list)
        for i, num in enumerate(nums):
            diff = target - nums[i]
            if hashmap[diff]:
                j = hashmap[diff].pop()
                ans = [j,i]
            else:
                hashmap[nums[i]].append(i)
        return ans


s = Solution()
nums = [1, 2, 2,3,4,5]
target = 9
print(s.threeSum(nums, target))  # [[0, 3], [1, 2]]




'''
nums = [1,2,2,7]
target = 9

ans = []
map={}
traverse s
    check diff = target - num[i] in map?
    if not:
        add num[i](map key) into map with i as index(map value)
        map[num: list[index1,index2, ...]]
    if yes:
        get first or last diff's value, which is index, from map, with i, store in ans(ans[i, diff's value])
        if not map[diff], del map[diff]
return ans


'''