
'''
Approach 5: Merge with Divide And Conquer
Intuition & Algorithm

This approach walks alongside the one above but is improved a lot. We don't need to traverse most nodes many times repeatedly

Pair up k lists and merge each pair.

After the first pairing, k lists are merged into k/2 lists with average 2N/k length, then k/4, k/8 and so on.

Repeat this procedure until we get the final sorted linked list.

Thus, we'll traverse almost N nodes per pairing and merging, and repeat this procedure about log 
2k times.


Complexity Analysis

Time complexity : O(Nlogk) where k is the number of linked lists.

We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
Sum up the merge process and we can get: O(∑ 
i=1
log 
2
​
 k
​
 N)=O(Nlogk)
Space complexity : O(1)

We can merge two sorted linked lists in O(1) space.
'''


from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		amount = len(lists)
		interval = 1
		run = 1
		while interval < amount:
			forEnd = amount - interval
			forInterval = interval * 2
			for i in range(0, forEnd, forInterval):
				toMerge = i + interval
				lists[i] = self.merge2Lists(lists[i], lists[toMerge])
				print(f'run:{run} forEnd:{forEnd} forInterval:{forInterval} i:{i} toMerge:{toMerge}')
			interval *= 2
			run += 1

		return lists[0] if amount > 0 else None

	def merge2Lists(self, l1, l2):
		head = point = ListNode(0)
		while l1 and l2:
			if l1.val <= l2.val:
				point.next = l1
				l1 = l1.next
			else:
				point.next = l2
				l2 = l2.next

			point = point.next

		if not l1:
			point.next = l2
		else:
			point.next = l1
		
		return head.next


# ===== 輔助方法 =====
def list_to_linkedlist(arr):
	dummy = ListNode(0)
	current = dummy
	for num in arr:
		current.next = ListNode(num)
		current = current.next
	return dummy.next

def linkedlist_to_list(node):
	result = []
	while node:
		result.append(node.val)
		node = node.next
	return result


# ===== 測試 =====
lists = [
	list_to_linkedlist([1, 5, 9, 13, 17, 21, 25, 29, 33, 37]),
	list_to_linkedlist([2, 6, 10, 14, 18, 22, 26, 30, 34, 38]),
	list_to_linkedlist([3, 7, 11, 15, 19, 23, 27, 31, 35, 39]),
	list_to_linkedlist([4, 8, 12, 16, 20, 24, 28, 32, 36, 40]),
	list_to_linkedlist([5, 9, 12, 16, 20, 28, 28, 32, 39, 55]),
	list_to_linkedlist([6, 9, 12, 13, 20, 24, 28, 35, 36, 48]),
	list_to_linkedlist([4, 6, 13, 18, 25, 27, 28, 32, 36, 88]),
	list_to_linkedlist([0, 41, 42, 43, 44, 45, 46, 47, 48, 49])
]

solution = Solution()
merged = solution.mergeKLists(lists)

print(f'結果：{linkedlist_to_list(merged)}')  # 預期輸出: [1,1,2,3,4,4,5,6]



'''
好 👌 我幫你把這份腳本拆解來解釋，它其實就是 LeetCode 23: Merge k Sorted Lists 的 Divide and Conquer 解法。

1. 類別與資料結構
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


這是單向鏈結串列 (linked list) 節點，每個節點有：

val: 當前數值

next: 下一個節點的參考

2. 主程式：mergeKLists
class Solution:
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
		amount = len(lists)   # 總共有多少個 list
		interval = 1          # 一開始每次合併相鄰的 1 個 list
		run = 1
		while interval < amount:  # 持續執行直到所有 list 合併完
			forEnd = amount - interval
			forInterval = interval * 2
			for i in range(0, forEnd, forInterval):
				print(f'run:{run} forEnd:{forEnd} forInterval:{forInterval}')
				# 把 lists[i] 和 lists[i+interval] 這兩個鏈表合併
				lists[i] = self.merge2Lists(lists[i], lists[i + interval])
			interval *= 2  # 每一輪合併後，下一次要合併的間隔加倍
			run += 1

		return lists[0] if amount > 0 else None

🎯 邏輯

一開始 interval=1，代表把相鄰的兩個 list 兩兩合併。

合併完後，下一次 interval=2，代表每次跨 2 個 list 再合併（例如 lists[0] 和 lists[2] 已經是合併過的結果）。

持續倍增 interval，直到只剩一個 list。

這就是 Divide and Conquer 的核心思想。

🔍 假設有 8 個 list：

interval=1 → 合併成 4 個 list

interval=2 → 合併成 2 個 list

interval=4 → 合併成 1 個 list (完成)

3. 兩個鏈表合併：merge2Lists
	def merge2Lists(self, l1, l2):
		head = point = ListNode(0)  # dummy node
		while l1 and l2:
			if l1.val <= l2.val:
				point.next = l1
				l1 = l1.next
			else:
				point.next = l2
				l2 = l1
				l1 = point.next.next
			point = point.next

		if not l1:
			point.next = l2
		else:
			point.next = l1

		return head.next


這裡做的就是 合併兩個有序鏈表 的標準演算法：

新建一個 dummy 頭節點（方便操作）。

point 從 dummy 出發，每次比較 l1 和 l2 當前值，把較小的接到結果鏈表後面。

更新 point，往下走。

如果某一個鏈表用完了，就直接把另一個鏈表接上。

回傳 dummy.next（跳過虛擬頭）。

⚠️ 不過你貼的版本有一個小錯誤：

else:
	point.next = l2
	l2 = l1
	l1 = point.next.next


這裡應該是：

else:
	point.next = l2
	l2 = l2.next


不然邏輯會跑錯 😅。

4. 輔助方法
def list_to_linkedlist(arr):
	dummy = ListNode(0)
	current = dummy
	for num in arr:
		current.next = ListNode(num)
		current = current.next
	return dummy.next

def linkedlist_to_list(node):
	result = []
	while node:
		result.append(node.val)
		node = node.next
	return result


list_to_linkedlist：把 Python list 轉成 linked list，方便建測資。

linkedlist_to_list：把 linked list 轉回 Python list，方便檢查輸出。

5. 測試流程
lists = [
	list_to_linkedlist([1,4,5]),
	list_to_linkedlist([1,3,4]),
	list_to_linkedlist([2,6])
]

solution = Solution()
merged = solution.mergeKLists(lists)

print(f'結果：{linkedlist_to_list(merged)}')  
# 預期輸出: [1,1,2,3,4,4,5,6]


流程就是：

準備 3 個有序鏈表。

呼叫 mergeKLists 合併。

轉換回 Python list，印出檢查。

✅ 總結腳本邏輯

使用 Divide and Conquer，每次兩兩合併鏈表。

每一輪合併的間隔 interval 倍增，直到合併成 1 條最終鏈表。

合併兩條鏈表用標準「歸併排序」方式。

輔助方法幫忙在 Python list 和 linked list 之間轉換。
'''