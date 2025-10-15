from typing import List

class Solution:
    def twoIntegerSumTarget(self, nums: List[int], target: int) -> List[List[int]]:
        hashMap = {}
        ans = []
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                list = []
                targetList = hashMap.get(target - nums[i])
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
nums = [1,2,2,7]
target = 9
ans = s.twoIntegerSumTarget(nums,target)
print(ans)


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