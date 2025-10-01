from typing import List
from collections import defaultdict

class Solution:
    def twoIntegerSumTarget(self, nums:List[int], target:int) -> List[List[int]]:




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