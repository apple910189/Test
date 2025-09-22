def FindMinimumInRotatedSortedArrary(nums):
	if len(nums) == 0:
		raise Exception('empty array')

	n = len(nums) - 1
	if nums[0]<=nums[n]:
		return nums[0] # case: not rotated
	right = n
	left = 0
	
	while right - left > 1:
		middle = (right+left)//2
		print(f'm: {middle} nums[m]:{nums[middle]}')
		if nums[middle] > nums[0]:
			print(f'l:{left}')
			left = middle
		else:
			print(f'r:{right}')
			right = middle

	return nums[right]

def FindMinimumInRotatedSortedArraryWithDuplicateElements(nums):
	if len(nums) == 0:  
		raise Exception("empty array")
	n = len(nums) - 1
	while n!=0 and nums[n] == nums[0]:
		n = n - 1
	if nums[0] <= nums[n]:
		return nums[0];
	left = 0
	right = n
	while right - left > 1:
		middle = (left + right) // 2
		if nums[middle] >= nums[0]:
			left = middle
		else:
			right = middle
	return nums[right]

def a(nums):
	if len(nums)==0:
		raise Exception('empty array')
	n = len(nums)-1
	while n!=0 and nums[0]==nums[n]:
		n = n - 1
	left = 0
	right = n
	while right - left > 1:
		middle = (right + left) // 2
		if nums[middle] >= nums[0]:
			left = middle
		else:
			right = middle
	return nums[right]

def calculate():
	# rate = 1.015
	Payment = 21
	totalMonth = 10
	if Payment%totalMonth == 0:
		pay = Payment//totalMonth
		print(f'pay: {pay}')
		return

	left = 0
	right = Payment

	while right - left > 1:
		middle = (left+right)//2
		if middle*(totalMonth)>=Payment:
			right = middle
		else:
			left = middle

	print(f'Payment per month: {right}')
	print('Payment for last month: ')





n1 = [10,11,12,13,14,1,2,3,4,5,6,7,8,9]
n2 = [14,1,2,3,4,5,6,7,8,9,10,11,12,13]
n3 = [2,3,4,5,6,7,8,9,10,11,12,13,14,1]
case1 = [3,4,5,1,2]
case2 = [4,5,6,7,0,1,2]
case3 = [11,13,15,17]
res1 = FindMinimumInRotatedSortedArrary(case1)
res2 = FindMinimumInRotatedSortedArrary(case2)
res3 = FindMinimumInRotatedSortedArrary(case3)

case4 = [1,3,5]
case5 = [2,2,2,0,1]
res4 = FindMinimumInRotatedSortedArraryWithDuplicateElements(case4)
res5 = FindMinimumInRotatedSortedArraryWithDuplicateElements(case5)
# result = FindMinimumInRotatedSortedArraryWithDuplicateElements(n5)

print(f'case1:{res1}')
print(f'case2:{res2}')
print(f'case3:{res3}')

print(f'case4:{res4}')
print(f'case5:{res5}')









