# mergeLinkedList (leetcode)

from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
	
	def get_next(self):
		return self.next
	
	def set_next(self, next_node):
		self.next = next_node

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		new = ListNode(-1)
		curr = new
		while l1 and l2:
			if l1.val <= l2.val:
				curr.next = l1
				l1 = l1.next
			else:
				curr.next = l2
				l2 = l2.next
			curr = curr.next
		if l1 is not None:
			curr.next = l1
		else:
			curr.next = l2
		return new.next

# ======= 工具函式 =======
def list_to_linked(lst):
	if not lst:
		return None
	head = ListNode(lst[0])
	curr = head
	print(lst[1:])
	for v in lst[1:]:
		curr.next = ListNode(v)
		curr = curr.next
	return head

def print_list(listName, node: Optional[ListNode]):
	"""把鏈結串列轉回字串輸出"""
	values = []
	while node:
		values.append(str(node.val))
		node = node.get_next()
	print(f'{listName}: {" -> ".join(values)}')

def print_address(nodeName, node: Optional[ListNode]):
	values = []
	while node:
		values.append(str(hex(id(node)))[5:10])
		node = node.next
	print(f'{nodeName}: {" -> ".join(values)}')


# ======= 測試 =======
list1 = [1,2,3]
list2 = [4,5]
list3 = [5,6]

l1 = list_to_linked(list1)
l2 = list_to_linked(list2)
l3 = list_to_linked(list3)

sol = Solution()
merged = sol.mergeTwoLists(l1, l2)
print_list('合併後結果：',merged)


# print('關於 linked list address 注意事項')
# p1 = ListNode(-1)
# print('\n ---------- 初始化 p2 = p1, 他們有相同的 head  ')
# p2 = p1
# print_address('p2',p2)
# print_address('p1',p1)
# print('\n ---------- 當 p2 = l1, 只有 p2 的 head 被改變')
# print_address('l1',l1)
# p2 = l1
# print_address('p2',p2)
# print_address('p1',p1)

# p3 = ListNode(-1)
# print('\n ---------- 初始化 p4 = p3, 他們有相同的 head ')
# p4 = p3
# print_address('p3',p3)
# print_address('p4',p4)
# print('\n ---------- 當 p4.next = l1, 因 p4/p3 有相同的 head ，所以他們的 next 同步改變 ')
# print_address('l1',l1)
# p4.next = l1
# print_address('p4',p4)
# print_address('p3',p3)






