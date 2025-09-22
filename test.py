def FindMinimumInRotatedSortedArraryWithDuplicateElements(nums):
	if len(nums) == 0:
		raise Exception('empty array')
	n = len(nums) - 1
	while n!=0 and nums[0] == nums[n]:
		n = n - 1
	if nums[0] <= nums [n]:
		return nums[0]
	right = n
	left = 0
	while right - left > 1:
		middle = (right+left)//2
		if nums[0] <= nums[middle]:
			left = middle
		else:
			right = middle
	return nums[right]


n1 = [10,11,12,13,14,1,2,3,4,5,6,7,8,9]
n2 = [14,1,2,3,4,5,6,7,8,9,10,11,12,13]
n3 = [2,3,4,5,6,7,8,9,10,11,12,13,14,1]
case4 = [1,3,5]
case5 = [2,2,2,0,1]
res4 = FindMinimumInRotatedSortedArraryWithDuplicateElements(case4)
res5 = FindMinimumInRotatedSortedArraryWithDuplicateElements(case5)

print(res4)
print(res5)


# [3,3,4,5,6]
# [3,3,4,2]
# [3,3,4,5,1,3]
# [3,3,2,3]

















