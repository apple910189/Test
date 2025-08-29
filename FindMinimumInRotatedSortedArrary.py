def FindMinimumInRotatedSortedArrary(nums):
	
	# case: empty array
	if len(nums) == 0: 
		raise Exception("empty array")
	
	n = len(nums) - 1
	# case: not rotated / one element / identical elements
	if nums[0] <= nums[n]:
		return nums[0]        
	
	left = 0
	right = n
	count = 1
	while right - left > 1:
		print(f'Run {count} -------------------------')
		middle = (left + right) // 2
		print(f'[info] left: [{str(left)}]({nums[left]}), right: [{str(right)}]({nums[right]}), middle: [{str(middle)}]({nums[middle]})')
		
		# case: compare middle with the leftmost
		# if middle >= leftmost, this means everything on the left of middle
		if nums[middle] > nums[0]:
			print(f'[if  ] middle({nums[middle]}) >= nums[0]({nums[0]})')
			print(f'[do  ] move left[{left}] to middle[{middle}]')
			left = middle
		else:
			print(f'[if  ] middle({nums[middle]}) < nums[0]({nums[left]})')
			print(f'[do  ] move right[{right}] to middle[{middle}]')
			right = middle
		print(f'[info] left: [{str(left)}]({nums[left]}), right: [{str(right)}]({nums[right]})')
		print()
		count = count+1
	return nums[right];

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
n4 = [4,5,1,2,3]
n5 = [2,2,3,1,2]
n6 = []
# result = FindMinimumInRotatedSortedArrary(n4)
# result = FindMinimumInRotatedSortedArraryWithDuplicateElements(n5)
result = a(n5)
print(result)

calculate()









